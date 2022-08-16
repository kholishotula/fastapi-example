from fastapi import APIRouter, Depends, status
from app import schemas
from config.database import get_mysql_db
from typing import List
from sqlalchemy.orm import Session
from repository import blog_repository
from utils import oauth2

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(get_mysql_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_new_blog(request: schemas.Blog, db: Session = Depends(get_mysql_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_mysql_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_by_id(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, request: schemas.Blog, db: Session = Depends(get_mysql_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(get_mysql_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.destroy(id, db)