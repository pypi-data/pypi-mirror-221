import json
from pprint import pprint
from time import time
import threading
import logging
from queue import Queue
from typing import Any, Dict

import uuid as uuid
from psycopg import sql
import psycopg
from decouple import config
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.security.api_key import APIKey
from starlette.responses import StreamingResponse
from uuid6 import uuid7
from loguru import logger
from nnext.server.lib.agents.base import AgentBase
from nnext.server.lib.agents.factory import AgentFactory
from nnext.server.lib.auth.api import get_api_key
from nnext.server.lib.auth.prisma import JWTBearer, decodeJWT
from nnext.server.lib.models.agent import Agent, PredictAgent
from nnext.server.lib.prisma import prisma

router = APIRouter()

import os
import redis
REDIS_STREAM_HOST=os.environ.get('REDIS_STREAM_HOST', "localhost")
REDIS_PASSWORD=os.environ.get('REDIS_PASSWORD')
red_stream = redis.StrictRedis(
    REDIS_STREAM_HOST, 6379, charset="utf-8",
    password=REDIS_PASSWORD, decode_responses=True)

@router.post("/agent", name="Create agent", description="Create a new agent")
async def create_agent(body: Agent):
    """Agents endpoint"""
    try:
        agent = prisma.agent.create(
            {
                "name": body.name,
                "type": body.type,
                "llm": json.dumps(body.llm),
                "hasMemory": body.hasMemory,
                "userId": decoded["userId"],
                "promptId": body.promptId,
            },
            include={"user": True},
        )

        return {"success": True, "data": agent}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e,
        )


@router.get("/agent", name="List all agents", description="List all agents")
async def read_agents():
    """Agents endpoint"""
    decoded = decodeJWT(token)
    agents = prisma.agent.find_many(
        where={"userId": decoded["userId"]},
        include={
            "user": True,
        },
        order={"createdAt": "desc"},
    )

    if agents:
        return {"success": True, "data": agents}

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="No agents found",
    )


@router.get("/agent/{agentId}", name="Get agent", description="Get a specific agent")
async def read_agent(agentId: str, token=Depends(JWTBearer())):
    """Agent detail endpoint"""
    agent = prisma.agent.find_unique(where={"id": agentId}, include={"prompt": True})

    if agent:
        return {"success": True, "data": agent}

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Agent with id: {agentId} not found",
    )


@router.delete(
    "/agent/{agentId}", name="Delete agent", description="Delete a specific agent"
)
async def delete_agent(agentId: str, token=Depends(JWTBearer())):
    """Delete agent endpoint"""
    try:
        prisma.agentmemory.delete_many(where={"agentId": agentId})
        prisma.agent.delete(where={"id": agentId})

        return {"success": True, "data": None}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e,
        )


@router.patch(
    "/agent/{agentId}", name="Patch agent", description="Patch a specific agent"
)
async def patch_agent(agentId: str, body: dict, token=Depends(JWTBearer())):
    """Patch agent endpoint"""
    try:
        prisma.agent.update(data=body, where={"id": agentId})

        return {"success": True, "data": None}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e,
        )


# @router.post(
#     "/agent/{agentId}/rxun",
#     name="Prompt agent",
#     description="Invoke a specific agent",
# )
# async def run_agent(
#     agentId: str,
#     body: dict,
#     background_tasks: BackgroundTasks
# ):
#
#     """Agent detail endpoint"""
#     sql_query_text = body.get("sql_query_text")
#     table = body.get("table")
#     output_column = body.get("output_column")
#     prompt = body.get("prompt")
#     pprint( prompt)
#
#     try:
#         print("Creating job...")
#         job = prisma.job.create(
#             {
#                 "id": str(uuid7()),
#             }
#         )
#
#         print(job)
#
#     except Exception as e:
#         logging.exception(e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=e,
#         )
#
#     for prompt_obj in prompt:
#         pprint(prompt_obj)
#         assert prompt_obj['type'] == 'paragraph'
#         filt_mention = list(filter(lambda x: 'type' in x and x['type'] == 'mention', prompt_obj['children']))
#
#         # If there is no column mentioned, skip.
#         if len(filt_mention) == 0:
#             continue
#
#         column_name = filt_mention[0]['column']
#
#     if column_name is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Column name cannot be empty.",
#         )
#
#     # PLAT DATABASE.
#     # For client data that displays on the platform.
#     PLAT_DB_HOST = 'nnextai-plat.coidzm0p67y1.us-east-2.rds.amazonaws.com'
#     PLAT_DB_PASS = 'vifrAdREchOD0O9us6d5'
#     PLAT_DB_USER = 'postgres'
#     print("Connecting to plat db", sql_query_text)
#
#     PLAT_DB_URL = f"postgresql://{PLAT_DB_USER}:{PLAT_DB_PASS}@{PLAT_DB_HOST}/platdb_b6ef_mango_tree"
#
#     print(PLAT_DB_URL)
#
#     _sql_obj= sql.SQL(sql_query_text)
#
#     async with await psycopg.AsyncConnection.connect(PLAT_DB_URL, autocommit=True) as plat_db_conn:
#         async with plat_db_conn.cursor() as acur:
#             print("running query", _sql_obj)
#             await acur.execute(_sql_obj)
#             print("Done executing")
#             await acur.fetchone()   # fetchone method seems to work - fetchall doesn't. It's not clear why fetchone works here while we want to fetch all the records.
#
#             # Really, this batch queue should be executed by the nnext framework.
#             async for record in acur:
#                 print(record)
#
#                 stream_key = "browser-b51c"
#                 stream_message = {
#                     'ts': time(),
#                     'payload': json.dumps({
#                         "_id": str(record[0]),
#                         "url": record[1],
#                         "prompt": prompt
#                     }),
#                     'job_id': str(job.id),
#                     "table": table,
#                     "output_col": output_column,
#                 }
#                 red_stream.xadd(stream_key, stream_message)
#                 print(f"Added elem to stream {stream_key}. Elem: {stream_message}")
#
#     print("YYY", column_name)
#
#     agent = prisma.agent.find_unique(
#         where={"id": agentId},
#         include={"prompt": True},
#     )
#
#     return {"status": "success"}
#
#     agent_base = AgentBase(agent=agent)
#     agent_strategy = AgentFactory.create_agent(agent_base)
#     agent_executor = agent_strategy.get_agent()
#     result = agent_executor(agent_base.process_payload(payload=input))
#     output = result.get("output") or result.get("result")
#     background_tasks.add_task(
#         agent_base.create_agent_memory,
#         agentId,
#         "HUMAN",
#         json.dumps(input.get("input")),
#     )
#     background_tasks.add_task(
#         agent_base.create_agent_memory, agentId, "AI", output
#     )
#
#     if config("NNEXT_TRACING"):
#         trace = agent_base._format_trace(trace=result)
#         background_tasks.add_task(agent_base.save_intermediate_steps, trace)
#
#         return {"success": True, "data": output, "trace": json.loads(trace)}
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Agent with id: {agentId} not found",
#     )


@router.post(
    "/agent/react/run",
    name="Prompt agent",
    description="Invoke a specific agent",
)
async def run_react_agent(
    # agentId: str,
    body: dict,
    background_tasks: BackgroundTasks
):

    """Agent detail endpoint"""
    sql_query_text = body.get("sql_query_text")
    table_name = body.get("table")
    output_column = body.get("output_column")
    prompt = body.get("prompt")

    try:
        print("Creating job...")
        job = prisma.job.create(
            {
                "id": str(uuid7()),
            }
        )

        print(job)

    except Exception as e:
        logging.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e,
        )

    # PLAT DATABASE.
    # For client data that displays on the platform.
    PLAT_DB_HOST = 'nnextai-plat.coidzm0p67y1.us-east-2.rds.amazonaws.com'
    PLAT_DB_PASS = 'vifrAdREchOD0O9us6d5'
    PLAT_DB_USER = 'postgres'
    print("Connecting to plat db", sql_query_text)

    PLAT_DB_URL = f"postgresql://{PLAT_DB_USER}:{PLAT_DB_PASS}@{PLAT_DB_HOST}/platdb_b6ef_mango_tree"

    _sql_obj= sql.SQL(sql_query_text)

    prompt_text = ''
    print()

    for prompt_obj in prompt:
        for child in prompt_obj['children']:
            if child.get('type') == 'mention':
                prompt_text += "@" + child['column']
            else:
                prompt_text += child['text']

    print("Prompt text:", prompt_text)

    async with await psycopg.AsyncConnection.connect(
        host=PLAT_DB_HOST,
        user=PLAT_DB_USER,
        password=PLAT_DB_PASS,
        dbname='platdb_b6ef_mango_tree',
        autocommit=True
    ) as plat_db_conn:
        async with plat_db_conn.cursor() as acur:
            logger.info(f"Connected to DB. Running query {_sql_obj}")
            await acur.execute(_sql_obj)
            # Really, this batch queue should be executed by the nnext framework.
            async for record in acur:
                print(record)

                stream_key = "nnext::instream::agent->browser"
                stream_message = {
                    'ts': time(),
                    'payload': json.dumps({
                        "_id": str(record[0]),
                        "url": record[1]
                    }),
                    'job_id': str(job.id),
                    "table_name": table_name,
                    "prompt": json.dumps(prompt),
                    "prompt_text": prompt_text,
                    "output_column": output_column,
                }
                red_stream.xadd(stream_key, stream_message)
                logger.debug(f"Added elem to stream {stream_key}. Elem: {stream_message}")

    # agent = prisma.agent.find_unique(
    #     where={"id": agentId},
    #     include={"prompt": True},
    # )

    return {"status": "successx"}

    agent_base = AgentBase(agent=agent)
    agent_strategy = AgentFactory.create_agent(agent_base)
    agent_executor = agent_strategy.get_agent()
    result = agent_executor(agent_base.process_payload(payload=input))
    output = result.get("output") or result.get("result")
    background_tasks.add_task(
        agent_base.create_agent_memory,
        agentId,
        "HUMAN",
        json.dumps(input.get("input")),
    )
    background_tasks.add_task(
        agent_base.create_agent_memory, agentId, "AI", output
    )

    if config("NNEXT_TRACING"):
        trace = agent_base._format_trace(trace=result)
        background_tasks.add_task(agent_base.save_intermediate_steps, trace)

        return {"success": True, "data": output, "trace": json.loads(trace)}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Agent with id: {agentId} not found",
    )
