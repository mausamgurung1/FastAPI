from fastapi import FastAPI

app = FastAPI()


@app.get('/home')
def home(limit=10,published:bool=True):
    
    if published:
        return (f'{limit} is total number ')
    
    else:
        return (f'{limit} in total')


@app.get('/')
def index():
    return {"data":{"name":"mausam"}}

@app.get('/about')
def about():
    return {'data':'this is the home page'}



@app.get('/blog/{id}')
    #fech the blog with id = id
def blog(id:int):#id:int only take a number
    return {'data':{id}}  


@app.get('/blog/{id}/comment')
def comment(id):
    return {'data':{'1', '2', '3'}}