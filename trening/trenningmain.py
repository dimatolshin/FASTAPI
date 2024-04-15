from typing import List
import uvicorn
from pydantic import BaseModel, Field

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def hello():
    return FileResponse('test.html')


@app.post('/postdata')
def post_data(username=Form(), userage=Form()):
    return {'name': username, 'age': userage}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
