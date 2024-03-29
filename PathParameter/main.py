from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}


@app.get("/users")
async def list_users():
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}

#You can declare path "parameters" or "variables" with the same syntax used by Python format strings

#In FastAPI, when multiple routes match a given request, FastAPI will return the response from the first matching route it encounters.
#Order matters

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get('/food/{food_item}')
async def get_food(food_item : FoodEnum):
    if food_item == FoodEnum.fruits:
        return {'food_item':food_item, 'message':'These are fruits'}
    if food_item.value == 'vegetables':
        return {'food_item':food_item, 'message':'These are vegetables'}
    return {'food_item':food_item, 'message':'These are chocolates'}
