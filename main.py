from fastapi import FastAPI, Request, Response, Header, status
from pydantic import BaseModel
import json
from routes import router1 
from routes import router2 

app = FastAPI()


app.include_router(router1.router, prefix="/hello")
app.include_router(router2.router, prefix="/world")
tasks = []
task_id = 1 

class TaskCreate(BaseModel):  # pydantic object, not dictionary
    title: str 
    description: str

@app.get('/', status_code=status.HTTP_200_OK) # decorator
# @app.post("/", status_code=201) # can also write this
def taskList():
    return {
        'tasks': tasks
    }


@app.get('/task')
def getTask(id: int, status: bool): 
    return {
        "id": id, 
        "status": status,
        "message": "Successfull"
    }

@app.post('/create-task')
def createTask(task: TaskCreate): 
    global task_id 
    tasks.append({
        "id": task_id,
        "title": task.title,
        "description": task.description
    })
    task_id = task_id + 1 
    return {
        "message": "Task created successfully",
        "tasks": tasks
    }


@app.get("/status/{id}", status_code=status.HTTP_200_OK)
def getStatus(id:int, response: Response):

    if id < 5:
        response.status_code = 404
        return {}

    

@app.get("/headers")
def headers(
    custom: str | None = Header(default=None)
): 
    
    # print("Request -header: ")
    # print(vars(request))
    # print(request.__dict__)

    # print("###############################################")
    # response.headers["my-header"] = "phone: motorola"
    # print(response.headers)
    return {
        "msg": "hi there"
    }



@app.get('/params/{id}', status_code=status.HTTP_200_OK)
def params(request: Request): 
    print(request.path_params)
    print("######")
    print(request.query_params.get("key"))
    return {
        "msg": "hi there"
    }


# getting body 
# path parameter /{id}
# query parameter /value=2&height=3
# response model @app.get(endpoint,response_model=model from pydantic)
# organizing routes into different files
# req,res header




# Things to learn
# status code 
"""
    | Express.js        | FastAPI                       |
    | ----------------- | ----------------------------- |
    | `req`             | `request`                     |
    | `req.headers`     | `request.headers`             |
    | `req.query`       | `request.query_params`        |
    | `req.params`      | `request.path_params`         |
    | `req.cookies`     | `request.cookies`             |
    | `res.status(404)` | `raise HTTPException(404)`    |
    | `res.json()`      | `return {...}`                |
    | `res.setHeader()` | `response.headers[...] = ...` |
    | `res.cookie()`    | `response.set_cookie()`       |
    | `async (req,res)` | `async def endpoint()`        |
    | middleware        | `Middleware` / dependencies   |
    | error middleware  | exception handlers            |
"""