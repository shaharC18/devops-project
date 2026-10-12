import os

import psycopg
from fastapi import FastAPI

DATABASE_URL = os.environ["DATABASE_URL"]

with psycopg.connect(DATABASE_URL) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title TEXT NOT NULL)")

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello DevOps!"}


@app.get("/tasks")
def get_tasks():
    with psycopg.connect(DATABASE_URL) as conn:
        rows = conn.execute("SELECT id, title FROM taskz ORDER BY id").fetchall()
    return [{"id": row[0], "title": row[1]} for row in rows]


@app.post("/tasks")
def add_task(title: str):
    with psycopg.connect(DATABASE_URL) as conn:
        row = conn.execute(
            "INSERT INTO tasks (title) VALUES (%s) RETURNING id", (title,)
        ).fetchone()
    return {"id": row[0], "title": title}
