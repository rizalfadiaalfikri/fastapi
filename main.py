from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": {"name" : "Rizal Fadia Al Fikri"}}

@app.get('/about/')
def about():
    return {"data" : 'about page'}