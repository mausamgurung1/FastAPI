from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return {"data":{"name":"mausam"}}

@app.get('/about')
def about():
    return {'data':'this is the home page'}