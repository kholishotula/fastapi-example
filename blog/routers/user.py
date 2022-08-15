from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database, hashing
from sqlalchemy.orm import Session

get_db = database.get_db
hash = hashing.Hash

router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_pwd = hash.encrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id} is not available')
    return user