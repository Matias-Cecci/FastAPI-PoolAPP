from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .users import UserBase

class AppointmentBase(BaseModel):
    date: Optional[datetime] = None

class AppointmentCreate(BaseModel):
    client_id: int
    employee_id: int
    date: datetime
    
class AppointmentUpdate(BaseModel):
    date: datetime

    class Config:
        from_attributes = True
        
class Appointment(AppointmentBase):
    id: int
    client_id: int
    employee_id: int
    client: UserBase  
    employee: UserBase
    
    class Config:
        from_attributes = True