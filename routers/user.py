from fastapi import APIRouter, Depends
from app import schemas
from sqlalchemy.orm import Session
from repository import user_repository
from config import database

get_db = database.get_mysql_db

router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_new_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_repository.create(request, db)
    

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user_repository.get_by_id(id, db)