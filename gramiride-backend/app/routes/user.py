from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.user_service import register_user

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    phone: str
    password: str

@router.post("/register/user")
def create_user(user: UserCreate):
    success = register_user(user.name, user.phone, user.password)
    if success:
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=400, detail="User already exists")
