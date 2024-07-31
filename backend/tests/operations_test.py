from httpx import AsyncClient


# POST: create task: high - priority, status - in_progress
async def test_post_tasks1(ac: AsyncClient):
    response = await ac.post("/tasks", json={"task": "test",
                                             "description": "test",
                                             "priority": "high",
                                             "status": "in_progress",
                                             "user_id": 1
                                             })

    assert response.status_code == 200


# POST: create task: priority - low, status - done
async def test_post_tasks2(ac: AsyncClient):
    response = await ac.post("/tasks", json={"task": "test",
                                             "description": "test",
                                             "priority": "middle",
                                             "status": "in_progress",
                                             "user_id": 1
                                             })

    assert response.status_code == 200


# GET: user created
async def test_get_tasks(ac: AsyncClient):
    response = await ac.get("/tasks", params={
                                              "user_id": 1,
                                              })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 2


# GET: user created: filter
async def test_get_tasks_with_filter(ac: AsyncClient):
    response = await ac.get("/tasks", params={
                                              "user_id": 1,
                                              "priority": "middle"
                                              })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1


# GET: no user created
async def test_get_tasks_no_user(ac: AsyncClient):
    response = await ac.get("/tasks", params={
                                              "user_id": 0,
                                              })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 0


# GET: check get tasks by id:
async def test_get_tasks_by_id(ac: AsyncClient):
    response = await ac.get("/tasks/1", params={
                                                "user_id": 1,
                                                })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1


# PUT: check get tasks by id:
async def test_put_tasks(ac: AsyncClient):
    response = await ac.put("/tasks/1", json={
                                                "task": "updated",
                                                "description": "updated",
                                                "priority": "low",
                                                "status": "done",
                                                "user_id": 1
                                                })

    assert response.status_code == 200
    assert response.json()["status"] == "The decsription of the task-1 is updated successfully"


# PATCH: change priority or status
async def test_patch_tasks(ac: AsyncClient):
    response = await ac.patch("/tasks/1", params={
                                                "priority": "middle",
                                                })

    assert response.status_code == 200
    assert response.json()["status"] == "The status & priority of the task-1 is updated successfully"


# DELETE: change priority or status
async def test_delete_tasks(ac: AsyncClient):
    response = await ac.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json()["status"] == "The task with id-1 deleted successfully"