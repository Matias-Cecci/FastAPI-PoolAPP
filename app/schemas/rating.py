from pydantic import BaseModel
from typing import Optional

class RatingBase(BaseModel):
    rating: int
    comment: Optional[str] = None

class RatingCreate(RatingBase):
    appointment_id: int
    client_id: int

class Rating(RatingBase):
    id: int
    appointment_id: int
    client_id: int
    
    class Config:
        from_attributes = True