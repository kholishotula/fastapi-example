from fastapi import FastAPI
from models.base import Base
from config.database import mysql_engine
from routers import blog, table, user, authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(table.router)

Base.metadata.create_all(mysql_engine)