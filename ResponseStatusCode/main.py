from fastapi import FastAPI

app = FastAPI()

'''
The same way you can specify a response model,
you can also declare the HTTP status code used for the response with the parameter status_code in any of the path operations
status_code is a parameter of the "decorator" method
'''

from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}



# You can use the convenience variables from fastapi.status.

from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

@app.post('/items/', status_code=status.HTTP_201_CREATED)
async def read_items(name: str):
    return name