from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from app import schemas
from constants.token_key import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from constants.error_types import CREDENTIAL_EXCEPTION

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise CREDENTIAL_EXCEPTION
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise CREDENTIAL_EXCEPTION
    return token_data