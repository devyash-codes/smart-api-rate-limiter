from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageResponse(BaseModel):
    message: str


class UserCreate(BaseModel):
    email: str
    name: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True



class APIKeyResponse(BaseModel):
    id: int
    key: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True



class RequestLogResponse(BaseModel):
    id: int
    endpoint: str
    status_code: int
    timestamp: datetime
    method:str

    class Config:
        from_attributes = True

class APIKeyResponse(BaseModel):
    id: int
    key: str
    created_at: datetime

    class Config:
        from_attributes = True