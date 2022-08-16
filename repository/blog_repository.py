from sqlalchemy.orm import Session
from app import schemas
from models.blogs import Blog
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_by_id(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with {id} is not available'
        )
    return blog

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} is not available')
    blog.update(request.dict())
    db.commit()
    return {'detail': 'success'}

def destroy(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'success'}