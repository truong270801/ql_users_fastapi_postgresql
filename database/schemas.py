from typing import List, Optional,Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import date


T = TypeVar('T')
class userSchema(BaseModel):
    firstName:Optional[str] = None
    lastName:Optional[str] = None
    maidenName:Optional[str] = None
    age:Optional[int] = None
    gender:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str] = None
    birthDate:Optional[date] = None
    address:Optional[str] = None
    city:Optional[str] = None
    university:Optional[str] = None

    class Config:
        orm_mode = True

class RequestUser(BaseModel):
    parameter: userSchema = Field(...)

class Response (GenericModel,Generic[T]):
    user: Optional[T]