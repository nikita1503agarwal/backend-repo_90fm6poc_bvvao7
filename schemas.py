from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
    name: str = Field(..., min_length=2)
    phone: str = Field(..., min_length=7, max_length=20)
    email: Optional[EmailStr] = None
    message: Optional[str] = Field(None, max_length=1000)
