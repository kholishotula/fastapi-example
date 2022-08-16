from sqlalchemy.orm import Session
from app import schemas
from models.users import User
from fastapi import HTTPException, status
from utils.hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = User(name=request.name, email=request.email, password=Hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id} is not available')
    return user

def get_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credential')
    return user