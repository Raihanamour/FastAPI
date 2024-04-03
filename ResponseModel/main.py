from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

from typing import Any


app = FastAPI()


'''
- By using the response_model parameter, you can ensure that your API responses are consistent, well-structured, and validated according to a predefined schema. 


- You can use the response_model parameter in any of the path operations:
@app.get()
@app.post()
@app.put()
@app.delete()


"response_model is a parameter of the "decorator" method (get, post, etc). Not of your path operation function, like all the parameters and body."

'''


# class Item(BaseModel):
#     name : str
#     description : str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []

# @app.post('/item/', response_model= Item)
# async def create_item(item:Item) -> Any:
#     return item

# @app.get('/item/', response_model= list[Item])
# async def read_item() -> Any:
#     return [
#         {'name': 'MacbookAir', 'price':120000},
#         {'name':'Alexa', 'tax':120, 'price':2500}
#     ]

# Return Type and Data Filtering

class BaseUser(BaseModel):
    username : str
    email: EmailStr
    fullname: str | None = None

class UserIn(BaseUser):
    password : str


@app.post('/user/')
async def create_user(user: UserIn) -> BaseUser:
    return user


# Other Return Type Annotations

'''
he most common case would be returning a Response directly 
'''

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


# Annotate a Response Subclass

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# Response Model encoding parameters

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal['foo','bar','baz']):
    return items[item_id]



#response_model_include and response_model_exclude

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]