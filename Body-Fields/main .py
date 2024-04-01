'''
In FastAPI, the Field class allows you to customize and validate request parameters and bodies. It's particularly useful when you need to add metadata or validation rules to your data models.
'''
from fastapi import FastAPI,Path,Query,Body
from typing import Annotated
from pydantic import Field, BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(None, title= 'the descripyion of the item',max_length= 200)
    price: float = Field(gt=0, title= 'Price should be greater than zero')
    tax : float | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id :  int,
    item : Annotated[Item,Body(embed = True)]
):
    results = {'item_id':item_id, 'item':item}

    return results
