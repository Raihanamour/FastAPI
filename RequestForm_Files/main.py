from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated

app = FastAPI()

'''
- You can define files and form fields at the same time using File and Form.
'''

@app.post('/files/')
async def upload_file(
    file : Annotated[bytes, File()],
    fileb : Annotated[UploadFile,File()],
    token :Annotated[str, Form()]
):
    return {
        'file_size': len(file),
        'token' : token,
        'fileb_content_type': fileb.filename
    }