from pydantic import BaseModel, EmailStr
from typing import Optional
from .user_roles import UserRole


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    
class UserCreate(UserBase):
    password: str
    role_id: int
    
class UserUpdate(UserBase):
    email: Optional[str]
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    password: Optional[str]
    
class User(UserBase):
    id: int
    role: UserRole
    
    class Config:
        from_attributes = True
        
class UserInDB(UserBase):
    id: int
    hashed_password: str
    
    class Config:
        from_attributes = True
    