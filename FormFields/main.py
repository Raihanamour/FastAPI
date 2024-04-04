from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()


'''
Recieve form fields instead of JSON
1. To use forms, first install python-multipart
    # pip install python-multipart
'''

@app.post('/login/')
async def login(username: Annotated[str,Form()],password: Annotated[str,Form()]):
    return { 'username': username}


