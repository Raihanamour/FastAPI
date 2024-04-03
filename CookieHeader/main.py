# Cookie Parameter

from fastapi import FastAPI, Body, Cookie, Header
from typing import Annotated

app = FastAPI()


@app.get('/items/')
async def read_items(cookie_id : Annotated[str | None, Cookie()] = None):
    return {'cookie_id': cookie_id}


# Header parameter


from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}


# duplicate headers

'''
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}


'''