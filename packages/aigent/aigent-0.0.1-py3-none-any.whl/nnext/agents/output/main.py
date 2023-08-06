#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 NNext, Co."

# Standard Libraries
import json
import os
from pprint import pprint

# External Libraries
import psycopg2
import asyncio
import redis
import logging

# Internal Libraries
None
META_DB_URL = os.environ.get("META_DB_URL")
red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
node_id = "0189190e-e2df-7282-b74f-9e0aea16e528"
node_short_code = node_id.split("-")[-2]
node_name = "nnext-out"

async def store_to_db(_id, workspace_id, payload, *args, **kwargs):

    with psycopg2.connect(META_DB_URL) as meta_db_conn:
        with meta_db_conn.cursor() as curs:
            # Retrieve the project from the DB.
            curs.execute(
                """
                SELECT name, slug FROM project WHERE id = %(id)s
                """,
                {"id": workspace_id}
            )
            project = curs.fetchone()

            # Construct the client db connection string.
            PLAT_DB_URL = os.path.join(
                os.environ.get("PLAT_DB_URL"), project[1]
            )
            print(PLAT_DB_URL, payload, json.loads(payload)['result'])

            with psycopg2.connect(PLAT_DB_URL) as plat_db_conn:
                with plat_db_conn.cursor() as client_curs:
                    # client_curs.execute(
                    #     """
                    #         ALTER TABLE table_name
                    #         ADD COLUMN new_column_name VARCHAR(255);
                    #     """,
                    #     {
                    #         "id": task_id,
                    #         "node_id": node_id,
                    #         "workspace_id": workspace_id,
                    #         "start_time": start_time,
                    #         "end_time": datetime.now(timezone.utc),
                    #         "results": json.dumps(response),
                    #         "flow_run_id": flow_run_id
                    #     }
                    # )

                    client_curs.execute(
                        """
                        INSERT INTO \"techstars-companies-sheet1\" (
                            _id, ai_col
                        )
                        VALUES (%(_id)s, %(ai_col)s)
                        ON CONFLICT (_id)
                        DO UPDATE SET
                        ai_col=EXCLUDED.ai_col;
                        """,
                        {
                            "_id": _id,
                            "ai_col": json.loads(payload)['result']
                        }
                    )
                    print(client_curs.query)



def run_task(*args, **kwargs):
    del_on_error = kwargs.get("del_on_error", False)
    stream_key = f"{node_name}-{node_short_code}"
    l = red.xread(count=50, streams={stream_key: 0}, block=1000)

    for _k in l:
        stream_key, stream_messages = _k

        for _j in stream_messages:
            message_id, message_data = _j

            try:
                asyncio.run(
                    store_to_db(
                        message_data['_id'], message_data['workspace_id'], message_data['payload']
                    )
                )
            except Exception as e:
                logging.exception(e)

                if del_on_error:
                    red.xdel(stream_key, message_id)

            red.xdel(stream_key, message_id)

        print("Done Processing Message batch")

while True:
    print(f"Starting user agent: {node_name}")
    while True:
        try:
            run_task()
        except Exception as e:
            print(e)