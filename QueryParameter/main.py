from enum import Enum

from fastapi import FastAPI

app = FastAPI()

# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]



@app.get('/items')
async def list_items(skip: int=0, limit:int=10):
    return fake_items_db[skip : skip+limit]

#Optional parameters¶

@app.get('/items/{item_id}')
async def get_items(item_id:str, q:str | None= None):
    if q:
        return {'item_id':item_id, 'q':q}
    return {'item_id':item_id}

#Query parameter type conversion¶
@app.get('/items/{item_id}')
async def get_items(item_id:str, q:str | None = None, short: bool= False):
    items  = {'item_id':item_id}
    if q:
        items.update({'q':q})
    if not short:
        items.update({'description':'If you want to define a query parameter short with a default value of False (boolean), you can do so in FastAPI by specifying its type as bool and providing the default value'})
    return items


#Multiple path and query parameters¶
@app.get('/user/{user_id}/items/{item_id}')
async def get_item_user(user_id:str, item_id:str, q:str | None= None, short: bool = False ):
    items = {'item_id':item_id, 'owner_id':user_id}

    if q:
        items.update({"q":q})
    if not short:
        items.update({'description':'If you want to define a query parameter short with a default value of False (boolean), you can do so in FastAPI by specifying its type as bool and providing the default value'})
    return items


#Required query parameters¶
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item