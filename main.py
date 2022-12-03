from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": "Blog list"}

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