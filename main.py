from fastapi import FastAPI

app = FastAPI()

tasks = []


@app.get("/")
def home():
    return {"message": "Hello DevOps!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def add_task(title: str):
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    return task
