from pydantic import BaseModel

class UserRoleBase(BaseModel):
    role_name: str
    
class UserRole(UserRoleBase):
    id: int

    class Config:
        from_attributes = True
        
