#You can declare examples of the data your app can receive.

# from fastapi import FastAPI
# from typing import Annotated
# from pydantic import BaseModel


# app = FastAPI()

# class Item(BaseModel):
#     name : str
#     description : str | None = None
#     price : float
#     tax : float | None = None

#     model_config = {
#         'json_schema_extra': {
#             'examples': [
#                 {
#                     'name': 'MacbookAir',
#                     'description' : 'An Apple Product',
#                     'price' : 120000,
#                     'tax' : 12000
#                 }
#             ]
#         }
#     }


# @app.put('/items/{item_id}')
# async def update_item(item_id:int, item: Item):
#     result = {'item_id':item_id, 'item':item}
#     return result

# Field additional arguments

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):

#     name : str = Field(examples=['MacbookAir'])
#     description: str |None =  Field(None, examples= ['An apple product'])
#     price : float = Field(examples= [ 120000])
#     tax : float | None = Field(None, examples=[1200])

# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item:Item):
#     result = {'item_id':item_id, 'item':item}
#     return result

'''
When using any of:

Path()
Query()
Header()
Cookie()
Body()
Form()
File()
ou can also declare a group of examples with additional information that will be added to their JSON Schemas inside of OpenAPI.
'''

# Body with examples


'''
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):

    name : str
    description : str | None = None
    price : float 
    tax : float | None = None


@app.put('/items/{item_id}')
async def update_item(
    item_id:int,
    item: Annotated[
        Item, 
        Body(
            examples=[
                {
                    'name' : 'Alexa',
                    'description' : 'Speech recognition',
                    'price': 2500,
                    'tax': 250

                }
            ]
    
        )
    ]
):
    result = {'item_id':item_id,'item':item}
    return result
'''


# Body with multiple examples 
# Using the openapi_examples Parameter 


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
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results