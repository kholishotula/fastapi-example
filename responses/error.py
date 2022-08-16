from pydantic import BaseModel

class ErrResponse(BaseModel):
    success: bool
    message: str

def NewErrorResponse(message):
    return ErrResponse(
        success=False,
        message=message
    )