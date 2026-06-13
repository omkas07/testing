from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from src.testing.models import UserTable
from src.testing.database import db
from sqlalchemy import select

app = FastAPI()

class User(BaseModel):
    name: str

@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: User
):
    db_user = UserTable(
        name = user.name
    )

    db.add(db_user)
    await db.flush()
    await db.commit()

    return db_user

@app.get("/")
async def list_users():
    result = await db.execute(select(UserTable))
    db_users = result.scalars().all()
    return db_users
