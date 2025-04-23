from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.user_service import register_user, login_user
from app.services.auth import create_access_token

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    phone: str
    password: str

class UserLogin(BaseModel):
    phone: str
    password: str

@router.post("/register/user")
def create_user(user: UserCreate):
    success = register_user(user.name, user.phone, user.password)
    if success:
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=400, detail="User already exists")

@router.post("/login")
def login(user: UserLogin):
    auth_user = login_user(user.phone, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": auth_user.phone})
    return {"access_token": token, "token_type": "bearer"}

