from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status

from ..token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

from ..hashing import Hash
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["authentication"]
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credential')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}