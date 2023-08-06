#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 NNext, Co."

# Standard Libraries
import json
import hashlib
from os import environ as env
from datetime import datetime, timezone

# External Libraries
import redis
from loguru import logger
import openai

CACHE_EXPIRATION_DURATION = 60 * 60 * 24 * 90 # 90 days
openai.api_key = env.get('OPENAI_API_KEY')

REDIS_CACHE_HOST=env.get('REDIS_CACHE_HOST', "localhost")
REDIS_PASSWORD=env.get('REDIS_PASSWORD')
red_cache = redis.StrictRedis(
    REDIS_CACHE_HOST, 6379, charset="utf-8",
    password=REDIS_PASSWORD, decode_responses=True)

def with_cache(prefix, *args, **kwargs):

    def wrapper(func):

        async def wrapped(*args, **kwargs):
            # logger.info(f"Wrapped NNextApp")
            # logger.info(f"{args, kwargs}")
            arg_str = f"{args, kwargs}"

            cache_key = hashlib.sha256(str(arg_str).encode('utf-8')).hexdigest()

            cache_key = f"{prefix}::elem->{cache_key}"
            read_cache = kwargs.pop('read_cache', True)
            write_cache = kwargs.pop('write_cache', True)

            if read_cache:
                cache_val = red_cache.get(cache_key)
                # print(f"cache-> {cache_key}>>{cache_val[:300] if cache_val else None}")

                if cache_val:
                    logger.debug('Found element in cache - returning cached results', cache_val)
                    try:
                        result_dict = json.loads(cache_val)
                        _result = json.loads(result_dict['result'])
                        return _result
                    except Exception as e:
                        return result_dict['result']

            if True:
                logger.debug('No cache found or skipping cache - running function')
                # print("Calling function", func, args, kwargs)

                try:
                    start_time = datetime.now(timezone.utc)
                    _result = await func(*args, **kwargs)
                    end_time = datetime.now(timezone.utc)
                    result_dict = {
                        "result": json.dumps(_result, default=str),
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

            return _result

        return wrapped

    return wrapper

@with_cache(prefix="nnext::fn-cache::openai_chat", ex=CACHE_EXPIRATION_DURATION)
async def openai_chat(messages, *args, **kwargs):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.to_dict()['choices'][0]["message"]["content"]