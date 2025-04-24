from pydantic import BaseModel, Field
from typing import Optional

class FeedbackCreate(BaseModel):
    ride_id: int
    rating: float = Field(..., ge=1, le=5)
    comment: Optional[str] = None

class FeedbackResponse(BaseModel):
    ride_id: int
    user_id: int
    driver_id: int
    rating: float
    comment: Optional[str]

    class Config:
        orm_mode = True
