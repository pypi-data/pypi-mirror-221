#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 NNext, Co."

# Standard Libraries
import asyncio
import inspect
import os
import hashlib
import jinja2
from abc import ABCMeta, abstractmethod
from collections.abc import Callable
import json
from datetime import datetime, timezone
from pprint import pprint, pformat

# External Libraries
import psycopg
import redis
import tiktoken
from loguru import logger
from uuid6 import uuid7
from psycopg import sql
import openai

# Internal Libraries

# Global Variables
from nnext.lib.core.decor import openai_chat

CACHE_EXPIRATION_DURATION = 60 * 60 * 24 * 90 # 90 days
TASK_EXPIRATION_DURATION = 60 * 60 * 24 * 2 # 48 Hours

PLAT_DB_HOST = 'nnextai-plat.coidzm0p67y1.us-east-2.rds.amazonaws.com'
PLAT_DB_PASS = 'vifrAdREchOD0O9us6d5'
PLAT_DB_USER = 'postgres'
PLAT_DB_NAME = 'platdb_b6ef_mango_tree'

REDIS_STREAM_HOST=os.environ.get('REDIS_STREAM_HOST', "localhost")
REDIS_CACHE_HOST=os.environ.get('REDIS_CACHE_HOST', "localhost")
REDIS_PASSWORD=os.environ.get('REDIS_PASSWORD')
red_stream = redis.StrictRedis(
    REDIS_STREAM_HOST, 6379, charset="utf-8",
    password=REDIS_PASSWORD, decode_responses=True)
red_cache = redis.StrictRedis(
    REDIS_STREAM_HOST, 6379, charset="utf-8",
    password=REDIS_PASSWORD, decode_responses=True)
openai.api_key = os.environ['OPENAI_API_KEY']

# logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
jinja_env = jinja2.Environment()

def _hasattr(C, attr):
    return any(attr in B.__dict__ for B in C.__mro__)


class _AbstractClass(metaclass=ABCMeta):
    __required_attributes__ = frozenset()

    @abstractmethod
    def run(self):
        self.count += 1

class CallableDFColumnAgent(_AbstractClass, Callable):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        logger.info("Initializing CallableDFColumnAgent", func, *args, **kwargs)

    def __call__(self, func):
        logger.debug("Initialized on first call", func)

        async def wrapper(*args, **kwargs):
            logger.debug("Wrapping NNextApp", func, *args, **kwargs)

            async def wrapped(*args, **kwargs):
                logger.debug("Wrapped NNextApp", args, kwargs)
                return await func.run(*args, **kwargs)

            return wrapped

        return wrapper

class CallableDFColumnTool(_AbstractClass, Callable):
    def __init__(self, func, name, *args, **kwargs):
        self.func = func
        self.tool_name = name
        logger.info("Initializing CallableDFColumnAgent", func, *args, **kwargs)

        self.instream_key = f"nnext::instream::tool->{self.tool_name}"
        self.last_processed_stream_key = f"{self.instream_key}::processed_pointer"
        self.last_processed_message_id = red_stream.get(self.last_processed_stream_key)

    def get_last_processed_message_id(self):
        last_processed_message_id = red_stream.get(self.last_processed_stream_key)
        if last_processed_message_id is None:
            last_processed_message_id = "0-0"

        return last_processed_message_id

    def set_last_processed_message_id(self, message_id):
        last_processed_message_id = self.get_last_processed_message_id()

        old_ts, old_seq = last_processed_message_id.split("-")
        old_ts, old_seq = int(old_ts), int(old_seq)

        new_ts, new_seq = message_id.split("-")
        new_ts, new_seq = int(new_ts), int(new_seq)

        if new_ts >= old_ts:
            last_processed_message_id = message_id
        elif new_ts == old_ts and new_seq >= old_seq:
            last_processed_message_id = message_id
        else:
            print("!!!")
            exit(3)

        red_stream.set(self.last_processed_stream_key, last_processed_message_id)

        return last_processed_message_id

    async def wait_func_inner(self, *args, **kwargs):
        last_processed_message_id = self.get_last_processed_message_id()
        l = red_stream.xread(count=3, streams={self.instream_key: last_processed_message_id}, block=1000)

        for _k in l:
            stream_key, stream_messages = _k
            for _j in stream_messages:
                message_id, message_data = _j

                correlation_id = message_data.get('correlation_id')
                payload = json.loads(message_data.get('payload'))
                agent = message_data.get('agent')

                arg_names = inspect.getfullargspec(self.func)[0]
                kwarg_names = inspect.getfullargspec(self.func)[2]

                args = [payload.get(arg_name, None) for arg_name in arg_names]
                args_dict = {arg_name: payload.get(arg_name, None) for arg_name in arg_names}

                arg_dict_str = json.dumps(args_dict, sort_keys=True)
                arg_dict_hash = hashlib.sha256(arg_dict_str.encode('utf-8')).hexdigest()
                self.last_instream_key = message_id

                read_cache = True
                write_cache = True
                cache_key = f"nnext::cache::agent-run::tool->{self.tool_name}::elem->{arg_dict_hash}"
                # read_cache = kwargs.get('read_cache', True)
                # write_cache = kwargs.get('write_cache', True)

                if read_cache:
                    cache_val = red_cache.get(cache_key)

                    if cache_val:
                        logger.debug('Found element in cache - returning cached results')
                        try:
                            result_dict = json.loads(cache_val)
                        except Exception as e:
                            print(e)
                    else:
                        logger.info('No cache found or skipping cache - running agent')

                        try:
                            start_time = datetime.now(timezone.utc)
                            tool_result = await self.func(*args)
                            end_time = datetime.now(timezone.utc)
                            result_dict = {
                                "payload": {"result": tool_result},
                                "status": "SUCCESS",
                                "start_time": start_time,
                                "end_time": end_time,
                            }
                        except Exception as e:
                            logger.exception(e)

                            result_dict = {
                                "payload": {"error": str(e)},
                                "status": "ERROR",
                            }
                        finally:
                            if write_cache:
                                red_cache.set(
                                    cache_key,
                                    json.dumps(result_dict, default=str),
                                    ex=CACHE_EXPIRATION_DURATION
                                )

                res_stream_key = f"nnext::outstream::agent->{agent}::tool->{self.tool_name}"
                red_stream.xadd(res_stream_key, {
                    'payload': json.dumps(result_dict, default=str),
                    'correlation_id': correlation_id,
                })
                self.set_last_processed_message_id(message_id)
                # red_stream.xdel(stream_key, message_id)

        return None

    async def wait_func(self, *args, **kwargs):
        count  = 0
        while True:
            await self.wait_func_inner()

            count += 0
            if count > 25:
                break

    def run(self, *args, **kwargs):
        logger.info("Running CallableDFColumnAgent", *args, **kwargs)
        self.new_event_loop = asyncio.new_event_loop()
        try:
            self.new_event_loop.run_until_complete(self.wait_func())
        except redis.exceptions.ConnectionError as redis_connection_error:
            pass
            logger.critical(f"Redis connection error: {redis_connection_error}. Is Redis running and variable 'REDIS_STREAM_HOST' set?")
        finally:
            self.new_event_loop.close()

    def __call__(self, func):
        logger.info("Initialized on first call", func)

        async def wrapper(*args, **kwargs):
            logger.info("Wrapping NNextApp", func, *args, **kwargs)

            async def wrapped(*args, **kwargs):
                logger.info("Wrapped NNextApp", args, kwargs)
                return await func.run(*args, **kwargs)

            return wrapped

        return wrapper

class Agent(object):
    def __init__(self, name, invoke_commands, tool_graph, prompt_template, *args, **kwargs):
        self.name = name
        self.invoke_commands = invoke_commands
        self.tool_graph = tool_graph
        self.prompt_template = jinja_env.from_string(prompt_template)
        self.result_stream_key_set = set()

        self.instream_key = f"nnext::instream::agent->{self.name}"
        self.last_processed_stream_key = f"{self.instream_key}::processed_pointer"
        self.last_processed_message_id = red_stream.get(self.last_processed_stream_key)
        # red_stream.xgroup_create(
        #     name=self.agent_stream_key,
        #     group_name='nnext::agent::result', 'nnext::agent::result::group', mkstream=True)
        logger.info(f"Initialized NNextAgent [name={name} invoke_commands={invoke_commands}]")

        self.new_event_loop = asyncio.new_event_loop()
        self.new_event_loop.run_until_complete(self.connect_to_db())

    def __del__(self):
        logger.info(f"Deconstructed NNextAgent [name={self.name}]")
        self.new_event_loop = asyncio.new_event_loop()
        self.new_event_loop.run_until_complete(self.connect_to_db())

    async def connect_to_db(self):
        self.data_db_conn = await psycopg.AsyncConnection.connect(
            host=PLAT_DB_HOST,
            user=PLAT_DB_USER,
            password=PLAT_DB_PASS,
            dbname=PLAT_DB_NAME,
            autocommit=True
        )

        self.data_db_cursor = self.data_db_conn.cursor()
        logger.debug("Connected to DB")

    async def disconnect_db(self):
        await self.data_db_conn.close()
        await self.data_db_cursor.close()

    def plan(self):
        raise NotImplementedError

    def get_last_processed_message_id(self):
        last_processed_message_id = red_stream.get(self.last_processed_stream_key)
        if last_processed_message_id is None:
            last_processed_message_id = "0-0"

        return last_processed_message_id

    def set_last_processed_message_id(self, message_id):
        last_processed_message_id = self.get_last_processed_message_id()

        old_ts, old_seq = last_processed_message_id.split("-")
        old_ts, old_seq = int(old_ts), int(old_seq)

        new_ts, new_seq = message_id.split("-")
        new_ts, new_seq = int(new_ts), int(new_seq)

        if new_ts > old_ts:
            last_processed_message_id = message_id
        elif new_ts == old_ts and new_seq > old_seq:
            last_processed_message_id = message_id
        else:
            print("!!!")
            exit(3)

        red_stream.set(self.last_processed_stream_key, last_processed_message_id)

        return last_processed_message_id

    # Send jobs to the agent tools.
    async def sow(self):
        last_processed_message_id = self.get_last_processed_message_id()
        # logger.debug(f"sow: stream_key: {self.instream_key}")
        l = red_stream.xread(count=5, streams={self.instream_key: last_processed_message_id}, block=500)

        # Iterate over the stream keys.
        for _k in l:
            stream_key, stream_messages = _k
            # Iterate over the message batch for that stream key.
            for _j in stream_messages:
                message_id, message_data = _j
                logger.info(f"{[stream_key, message_id, message_data]}")
                tool_name = self.tool_graph['tools']["browser"].get('name')
                logger.info(tool_name)

                tool_stream_key = f"nnext::instream::tool->{tool_name}"

                payload = json.loads(message_data['payload'])
                prompt_text = message_data['prompt_text']
                output_column = message_data['output_column']
                table_name = message_data['table_name']
                correlation_id = payload.get('_id')

                red_stream.xadd(tool_stream_key, {
                    'payload': json.dumps(payload),
                    'correlation_id': correlation_id,
                    'agent': self.name,
                })

                task_key = f"nnext::task-pending::agent->{self.name}::correlation_id->{correlation_id}"
                red_cache.set(
                    task_key,
                    json.dumps({}, default=str),
                    ex=CACHE_EXPIRATION_DURATION
                )

                prompt_text_key = f"nnext::prompt-text::agent->{self.name}::correlation_id->{correlation_id}"
                red_cache.set(
                    prompt_text_key,
                    json.dumps({
                        "prompt_text": prompt_text,
                        "output_column": output_column,
                        "table_name": table_name
                    }, default=str),
                    ex=CACHE_EXPIRATION_DURATION
                )

                self.last_sow_key_processed = message_id

                self.set_last_processed_message_id(message_id)

    # Gather results from the result stream and place them into a set.
    async def reap(self):
        tool_name = self.tool_graph['tools']["browser"].get('id')

        # Iterate over all the tools and get their results.
        tool_stream_key_map = {}
        for tool_key, tool in self.tool_graph['tools'].items():
            tool_stream_key = f"nnext::outstream::agent->{self.name}::tool->{tool.get('id')}"
            tool_stream_key_map[tool_stream_key] = 0
        l = red_stream.xread(count=3, streams=tool_stream_key_map, block=5)

        # Iterate over the stream keys.
        for stream_key, stream_messages in l:
            # Iterate over the message batch for that stream key.
            for message_id, message_data in stream_messages:
                red_stream.xdel(stream_key, message_id)

                correlation_id = message_data.get('correlation_id')
                payload = message_data.get('payload')

                logger.info(correlation_id, pformat(payload))

                result_key = f"nnext::memory::agent->{self.name}::tool->{tool_name}[0]::elem->{correlation_id}"

                red_stream.set(result_key, json.dumps({
                    'payload': payload,
                }))

    async def collate(self):
        key_prefix = f"nnext::task-pending::agent->{self.name}::correlation_id->*"
        for key in red_stream.scan_iter(key_prefix):
            correlation_id = key.split("::correlation_id->")[1]

            tools_result_set_complete = True
            tool_result_map = {}
            # Check if all tools have completed.
            for tool_key, tool in self.tool_graph['tools'].items():
                tool_output_template = tool.get('output')
                tool_results = red_stream.get(
                    f"nnext::memory::agent->{self.name}::tool->{tool.get('id')}[0]::elem->{correlation_id}"
                )
                if tool_results is None:
                    tools_result_set_complete = False
                    break

                tool_results = tool_results
                tool_result_map[tool_output_template] = tool_results

            if tools_result_set_complete:
                prompt_text_key = f"nnext::prompt-text::agent->{self.name}::correlation_id->{correlation_id}"

                self.prompt_template
                llm_prompt = red_cache.get(prompt_text_key)
                if llm_prompt:
                    llm_prompt = json.loads(llm_prompt)
                    prompt_text = llm_prompt.get('prompt_text')

                    if "$GPT" in prompt_text:
                        prompt_text = prompt_text.split("$GPT")[1]

                    tool_result_map['llm_prompt'] = prompt_text

                context = self.prompt_template.render(tool_result_map)

                enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
                tokenized = enc.encode(context)

                tokenized = tokenized[:3500]
                tokenized_text = enc.decode(tokenized)

                chat_messages = [
                    {"role": "system", "content": "Given the following content extracted from a webpage"},
                    {"role": "user", "content": tokenized_text},
                    {"role": "assistant", "content": "Thanks. I will now use this information to generate a prompt."},
                    {"role": "user", "content": prompt_text}
                ]

                # Call OpenAI API.
                response = await openai_chat(chat_messages)
                # response = await openai_chat(chat_messages, read_cache=False, write_cache=True)

                red_stream.delete(key)

                logger.debug(f"openai Result-->> {pformat(response)}")

                result_key = f"nnext::agent-results::agent->{self.name}::correlation_id->{correlation_id}"
                red_cache.set(result_key, response, ex=CACHE_EXPIRATION_DURATION)

                # Store results in Redis and Postgres.
                output_column = llm_prompt.get('output_column')
                table_name = llm_prompt.get('table_name')

                _sql_stmt = sql.SQL(
                    """
                    INSERT INTO {} (_id, {})
                    VALUES (%(_id)s, %(result)s)
                    ON CONFLICT (_id)
                    DO UPDATE SET
                    {}=EXCLUDED.{};
                    """
                ).format(
                    sql.Identifier(table_name),
                    sql.Identifier(output_column),
                    sql.Identifier(output_column),
                    sql.Identifier(output_column)
                )

                print(_sql_stmt.as_string(self.data_db_cursor))

                try:

                    await self.data_db_cursor.execute(_sql_stmt, {
                        "_id": correlation_id,
                        "result": response
                    })
                except Exception as e:
                    logger.error(e)
                    logger.error(f"Error inserting into table {table_name}.")


    async def wait_func(self, *args, **kwargs):
        sow_co = self.sow()
        reap_co = self.reap()
        collate_co = self.collate()

        await sow_co
        await reap_co
        await collate_co

        return None

    def add_tool(self, tool):
        raise NotImplementedError

    def add_link(self, source, target):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        self.new_event_loop = asyncio.new_event_loop()
        try:
            while True:
                self.new_event_loop.run_until_complete(self.wait_func())
                # break

        except redis.exceptions.ConnectionError as redis_connection_error:
            logger.critical(
                f"Redis connection error: {redis_connection_error}. Is Redis running and variable 'REDIS_STREAM_HOST' set?")
        except Exception as e:
            logger.exception(e)
            logger.critical(f"Exception: {e}")
        finally:
            self.new_event_loop.close()

class Tool(object):
    def __init__(self, name, invoke_commands, *args, **kwargs):
        self.name = name
        self.invoke_commands = invoke_commands
        logger.info(f"Initializing Tool: [name='{name}' invoke_commands='{invoke_commands}']")

    def __call__(self, func):
        logger.info(f"Running Tool event loop for [name={self.name}]", func)
        c = CallableDFColumnTool(func, name=self.name, invoke_commands=self.invoke_commands)

        return c

    def listen(self):
        logger.info("Listening to NNextApp", self.name)
        pass