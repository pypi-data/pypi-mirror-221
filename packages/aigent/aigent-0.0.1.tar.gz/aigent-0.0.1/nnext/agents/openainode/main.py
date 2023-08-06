#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 NNext, Co."

# Standard Libraries
import json
import os
from pprint import pprint
from datetime import datetime, timezone
import logging

# External Libraries
from time import time
import psycopg
import asyncio
import redis
import openai
from uuid6 import uuid7
import tiktoken

# Internal Libraries
None

META_DB_URL = os.environ.get("META_DB_URL")
red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
openai.api_key = os.environ['OPENAI_API_KEY']
node_id = "01891803-f280-775f-99c9-36b1750b872f"
node_short_code = node_id.split("-")[-2]
node_name = "openai-chat"

async def run_prompt(prompt, context, *args, **kwargs):
    start_time = datetime.now(timezone.utc)
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokenized = enc.encode(context)
    print("Running Prompt")
    tokenized = tokenized[:3500]
    tokenized_text = enc.decode(tokenized)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a web scrapping assistant"},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Enter the context extracted from the browser below"},
            {"role": "user", "content": tokenized_text}
        ]
    )

    return response

    with psycopg.connect(META_DB_URL) as conn:
        with conn.cursor() as curs:
            task_id = str(uuid7())

            curs.execute(
                """
                INSERT INTO agent.agent_run (id, node_id, workspace_id, start_time, end_time, results, flow_run_id)
                VALUES (%(id)s, %(flow_run_id)s, %(workspace_id)s, %(start_time)s, %(end_time)s, %(results)s, %(flow_run_id)s);
                """,
                {
                    "id": task_id,
                    "node_id": node_id,
                    "workspace_id": workspace_id,
                    "start_time": start_time,
                    "end_time": datetime.now(timezone.utc),
                    "results": json.dumps(response),
                    "flow_run_id": flow_run_id
                }
            )

    # Send the results to the Output Node
    output_node_id = "0189190e-e2df-7282-b74f-9e0aea16e528"
    output_node_short_code = output_node_id.split("-")[-2]
    output_node_name = "nnext-out"
    output_stream_key = f"{output_node_name}-{output_node_short_code}"

    print(f"Sending Results to Output Node: {output_stream_key}")
    stream_message = {
        '_id': _id,
        'ts': time(),
        'payload': json.dumps({"result": response['choices'][0]['message']['content']}),
        'workspace_id': workspace_id,
        'flow_run_id': flow_run_id
    }
    red.xadd(output_stream_key, stream_message)

    print("Done running OpenAI Chat Prompt")


def run_task(*args, **kwargs):
    stream_key = f"{node_name}-{node_short_code}"

    l = red.xread(count=50, streams={stream_key: 0}, block=1000)

    for _k in l:
        stream_key, stream_messages = _k

        for _j in stream_messages:
            message_id, message_data = _j

            try:
                asyncio.run(
                    run_prompt(
                        message_data['_id'], message_data['payload'], message_data['workspace_id'], message_data['flow_run_id']
                    )
                )
            except Exception as e:
                logging.exception(e)

            red.xdel(stream_key, message_id)

        print("Done Processing Message batch")