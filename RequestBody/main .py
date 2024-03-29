from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# A request body is data sent by the client to your API. A response body is the data your API sends to the client.

#Create your data model
class Item(BaseModel):
    name : str
    description: str | None = None
    price : float 
    tax : float | None = None


#Declare it as a parameter
@app.post('/items')
async def create_item(item:Item):
    item_dict = item.dict()
    if item.tax:
        final_price = item.price + item.tax
        item_dict.update({'price including tax':final_price})
    return item_dict

@app.put('/items/{item_id}')
async def create_item_put(item_id:int, item: Item, q:str| None= None):
    result = {'item_id':item_id, **item.dict()}
    if q:
        result.update({'q':q})
    return result

