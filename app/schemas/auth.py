from pydantic import BaseModel, EmailStr
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenRequest(BaseModel):
    email: EmailStr
    password: str
    
class LoginRequest(BaseModel):
    email: str
    password: str