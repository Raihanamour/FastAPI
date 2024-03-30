#First, import Path from fastapi, and import Annotated:

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()

# declare the same type of validations and metadata for path parameters with Path

@app.get('/items/{item_id}')
async def item_validation(
    *,
    item_id: int=Path(..., title= "Id ofthe item to get", ge=10,le=100), 
    q:str = 'hello',
    #Number validations: floats
    size :float = Query(..., gt=0,le=9.5)

):
    result = {'item_id':item_id}
    if q:
        result.update({'q':q})
    return result



#Prefer to use the Annotated version if possible.


'''

# @app.get("/items_validation/{item_id}")
# async def read_items(
#     *,
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


'''
