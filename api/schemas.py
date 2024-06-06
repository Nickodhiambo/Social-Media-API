from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    

    class Config:
        from_attributes=True


class ResponseModel(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserRes
    
    class Config:
        from_attributes=True

class VotesOut(ResponseModel):
    ResponseModel: ResponseModel
    votes: int

    class Config:
        from_attributes=True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attribute = True


class TokenData(BaseModel):
    id: Optional[str] = None


class VoteData(BaseModel):
    post_id: int
    dir: conint(le=1) 