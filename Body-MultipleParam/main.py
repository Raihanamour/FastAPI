from fastapi import FastAPI,Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price : float
    tax : float |None = None

class User(BaseModel):
    username: str 
    fullname : str | None = None

@app.put('/items/{item_id}')
async def update_item(
    *,
    item_id: int = Path(..., title= 'Id of the parameter to get', ge=0, le=100),
    q : str | None = None,
    item : Item | None = None,
    user : User 
    
):
    results = {'item_id': item_id}
    if q:
        results.update({'q':q})
    if item:
        results.update({'item':item})
    if user:
        results.update({'user':user})
    return results



#using Annotate


'''
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


'''



#Embed a single body parameter

'''
If you only have a single item body parameter from a Pydantic model Item.
By default, FastAPI will then expect its body directly.

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


'''