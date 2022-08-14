from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# @app is path operation decorator
@app.get('/blog')
# path operation function
def index(page = 1, limit = 10, published: Optional[bool] = False):
    if published:
        return {'data': f'page {page} with {limit} published blogs from the db'}
    else:
        return {'data': f'page {page} with {limit} blogs from the db'}

# it should be defined first before the /blog/{id}
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int, page = 1, limit = 10):
    return {'data': {'1', '2'}}
