from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog/')
def index(limit = 10, published : bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published Blogs from the db"}
    else:
        return {"data": f"{limit} Blogs from the db"}
@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id):
    # fetch blog with id = id
    return {"data" : id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data' : {'1', '2'}}