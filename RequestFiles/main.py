# from fastapi import FastAPI, File, UploadFile
# from typing import Annotated

# app = FastAPI()

'''
You can define files to be uploaded by the client using File.
    - uploaded files are sent as "form data".
    - File is a class that inherits directly from Form.
    - Import File and UploadFile from fastapi
    - Use File, bytes, and UploadFile to declare files to be uploaded in the request, sent as form data.
'''


# @app.post('/files/')
# async def create_file(file: Annotated[bytes,File()]):
#     return {'file_size': len(file)}


# # FILE PARAMETER WITH UploadFile

# @app.post('/upload_files/')
# async def create_upload_file(file: UploadFile):
#     return {'file_name': file.filename}


'''
UploadFile has the following async methods
    - write(data)
    - read(size)
    - seek(offset)
    - close()
'''



# OPTIONAL FILE UPLOAD

# from fastapi import FastAPI, File, UploadFile
# from typing import Annotated


# app = FastAPI()

# @app.post('/files/')
# async def create_file(file: bytes | None = File(None)):
#     if not file:
#         return { 'message': 'no file upload'}
#     else:
#         return {'file_size': len(file)}


# @app.post('/upload_file/')
# async def create_upload_file(file: UploadFile | None = None):
#     if not file:
#         return {'message':'no file upload'}
#     else:
        # return { 'file_name': file.filename}


# UploadFile WITH ADDITIONAL METADATA


# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(
#     file: Annotated[UploadFile, File(description="A file read as UploadFile")],
# ):
#     return {"filename": file.filename}



# MULTIPLE FILE UPLOADS
'''
It's possible to upload several files at the same time.
You will receive, as declared, a list of bytes or UploadFiles.
'''

# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.post("/files/")
# async def create_files(files: Annotated[list[bytes], File()]):
#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(files: list[UploadFile]):
#     return {"filenames": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)


# MULTIPLE FILE UPLOAD WITH ADDITIONAL METADATA

from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)