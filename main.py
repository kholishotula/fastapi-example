from fastapi import FastAPI
from app import models
from app.database import mysql_engine
from app.routers import blog, table, user, authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(table.router)

# models.Base.metadata.create_all(sqlite_engine)
models.Base.metadata.create_all(mysql_engine)