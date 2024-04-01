# BODY - NESTED MODELS
'''
With FastAPI, you can define, validate, document, and use arbitrarily deeply nested models
'''

from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl   #Special types and validation
    name: str

class Item(BaseModel):
    name : str 
    description : str | None = None
    price : float
    tax : float | None = None
    # tags : list = []
    tags : set[str] = set()
    # image: Image 
    images: list[Image] | None = None  #Attributes with lists of submodels

#Deeply nested models¶

class Offer(BaseModel):
    name: str
    description: str | None = None
    price : float
    items : list[Item]




@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    result = {'item_id':item_id, 'item':item}
    return result


@app.post('/offers')
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer

#Bodies of pure lists

@app.post('/images/multiple')
async def multiple_image(images: list[Image]):
    return images


#Bodies of arbitrary dicts
@app.post('/index_weights')
async def create_weight(weight = dict[int, float]):
    return weight