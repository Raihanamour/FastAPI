# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr


# app = FastAPI()

# class UserBase(BaseModel):
#     user_name: str
#     email : EmailStr
#     fullname: str | None = None

# class UserIn(UserBase):
#     password : str

# class UserOut(UserBase):
#     pass

# class UserInDB(UserBase):
#     hashed_password : str

# def fake_password_hasher(raw_password: str):
#     return 'supersecret' + raw_password

# def fake_save_user(user_in : UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.model_dump(),hashed_password= hashed_password)
#     print('User Saved!!')
#     return user_in_db

# @app.post('/user/', response_model= UserOut)
# async def create_user(user_in : UserIn):
#     user_saved = fake_save_user(user_in)

#     return user_saved


# UNION OR ANYOF

'''
You can declare a response to be the Union of two types, that means, that the response would be any of the two.
import union from typing
'''


# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Union, Literal

# app = FastAPI()


# class BaseItem(BaseModel):
#     type: str
#     description: str

# class CarItem(BaseItem):
#     type: str = 'car'

# class PlaneItem(BaseItem):
#     type: str = 'plane'
#     size : int



# items = {
#     'item1': {
#         'type': 'car',
#         'description':'All my friends drive a low rider'
#     },
#     'item2':{
#         'type':'plane',
#         'description': 'Music is my aeroplane, its my aeroplane',
#         'size': 5

#     }
# }

# @app.get('/items/{item_id}', response_model= Union[PlaneItem, CarItem])
# async def read_item(item_id : Literal['item1','item2']):
#     return items[item_id]



# LIST OF MODELS

'''
You can declare responses of lists of objects.
use list
'''

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str


# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/items/", response_model=list[Item])
# async def read_items():
#     return items

# RESPONSE WITH ARBITRARY DICT

'''
declare a response using a plain arbitrary dict, declaring just the type of the keys and values, without using a Pydantic model.
use dict
'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}