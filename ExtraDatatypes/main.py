
# from fastapi import FastAPI, Body
# from typing import Annotated

# from uuid import UUID
# from datetime import datetime, time, timedelta


# app = FastAPI()


# @app.put('/items/{item_id}')
# async def read_items(
#     item_id : UUID,           #A standard "Universally Unique Identifier
#     start_date_time : Annotated[datetime | None, Body()] = None,
#     end_date_time : Annotated[datetime | None, Body()] = None,
#     repeat_at : Annotated[time | None, Body()] = None,
#     process_after : Annotated[timedelta | None, Body()] = None

# ):
#     start_process = start_date_time + process_after
#     duration = end_date_time - start_date_time
#     return {
#         'item_id' : item_id,
#         'start_date_time' : start_date_time,
#         'end_date_time' : end_date_time,
#         'repeat_at' : repeat_at,
#         'process_after' : process_after,
#         'start_process'  : start_process,
#         'duration' : duration

#     }



