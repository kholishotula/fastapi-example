from fastapi import HTTPException, status

NOT_FOUND = "Error Not Found"
SERVER_ERROR = "Internal Server Error"

CREDENTIAL_EXCEPTION = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )