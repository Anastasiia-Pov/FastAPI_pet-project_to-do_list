import json
from bson import ObjectId
import bson
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.requests import Request
from pymongo import AsyncMongoClient
from mongo_db_operations.mongodb_task_models import TaskCreate, GetTaskbyID, UpdateTask
from config import MONGO_DB

router_mongo = APIRouter(
    tags=["Tasks"]
)


@router_mongo.post('/tasks', summary='Add new task')
async def add_task(request: Request,
                   newtask: TaskCreate):
    """
    Create a task with all the information:

    - **task**: each task must have a name
    - **description**: optional description
    - **priority**: each task must have priority (low, middle, high)
    - **status**: each task must have status (waiting, in_progress, done)
    - **username**: each task must have a username (to whom a task belongs to)
    """
    try:
        task = jsonable_encoder(newtask)
        new_task = await request.app.database["tasks"].insert_one(task)
        new_task_id = new_task.inserted_id
    # printing for debugging
    # print(new_task_id)
    # print(type(new_task_id)) # <class 'bson.objectid.ObjectId'>
        return f'''Task with id {new_task_id} successfully added'''
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# получение задачи по username
@router_mongo.get('/tasks', summary='Get all task')
async def get_tasks(username: str,
                    request: Request):
    """
    Get tasks according to the request:
        - **username**: user whose tasks must be presented
    """
    tasks_cursor = request.app.database["tasks"].find({"username": username}, {"_id": False,})
    # Convert cursor to list
    tasks_list = await tasks_cursor.to_list(length=None)

    # printing for debugging
    # print(tasks_list)

    # If no tasks found, raise an HTTP exception
    if not tasks_list:
        raise HTTPException(status_code=404, detail="No tasks found for the given username")

    # Return the list of tasks
    return tasks_list


# получение задачи по id
# path parameter
@router_mongo.get('/tasks/{id}', summary='Get task by id via path parameter')
async def get_task_by_id(username: str,
                         id: str,
                         request: Request):
    """
    Get task by user_id and id:

    - **user_id**: whose tasks must be presented
    - **id**: id of the task
    """
    try:
        task = await request.app.database["tasks"].find_one({"username": username,
                                                             "_id": ObjectId(id)})
        if task:
            del task['_id']
            del task['username']
            return task
        else:
            raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# редактирование задачи
@router_mongo.put('/tasks/{id}', summary='Edit a task by id')
async def edit_task(id: str,
                    username: str,
                    update_task: UpdateTask,
                    request: Request):
    """
    Update a task with all the information:

    - **id**: id of the task
    - **task**: each task must have a name
    - **username**: each task must have a user (to whom a task belongs to)
    """
    try:
        task = await request.app.database["tasks"].find_one({"username": username,
                                                             "_id": ObjectId(id)})
        if task:
            task = await request.app.database["tasks"].update_one({"username": username,
                                                                   "_id": ObjectId(id)},
                                                                  {'$set': {"task": update_task.task,
                                                                             "description": update_task.description,
                                                                             "priority": update_task.priority,
                                                                             "status": update_task.status}})
            return f"Task with id {id} successfully updated!"
        else:
            raise HTTPException(status_code=404, detail=f"There is no task with the id {id}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
