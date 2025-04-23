from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.driver_service import register_driver, login_driver
from app.services.auth import create_access_token

router = APIRouter()

class DriverCreate(BaseModel):
    name: str
    phone: str
    vehicle_number: str
    vehicle_type: str
    password: str

class DriverLogin(BaseModel):
    phone: str
    password: str

@router.post("/register/driver")
def create_driver(driver: DriverCreate):
    success = register_driver(driver.name, driver.phone, driver.vehicle_number, driver.vehicle_type, driver.password)
    if success:
        return {"message": "Driver registered successfully"}
    raise HTTPException(status_code=400, detail="Driver already exists")

@router.post("/login/driver")
def login(driver: DriverLogin):
    auth_driver = login_driver(driver.phone, driver.password)
    if not auth_driver:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": auth_driver.phone})
    return {"access_token": token, "token_type": "bearer"}
