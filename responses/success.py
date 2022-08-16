from typing import Any, Optional
from pydantic import BaseModel

class SuccessResponse(BaseModel):
    success: bool
    data: Optional[Any] = None

def NewSuccessResponse(data: Optional[Any] = None):
    return SuccessResponse(
        success=True,
        data=data
    )