from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.ride_service import create_ride, get_pending_rides, accept_ride, update_ride_status
from app.services.auth import decode_access_token
from fastapi.security import OAuth2PasswordBearer
from app.services.user_service import get_user_by_phone
from app.services.driver_service import login_driver

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class RideRequest(BaseModel):
    pickup_location: str
    drop_location: str

class RideAccept(BaseModel):
    ride_id: int

class RideStatusUpdate(BaseModel):
    ride_id: int
    status: str  # ongoing, completed, cancelled

@router.post("/user/request-ride")
def request_ride(data: RideRequest, token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    user_phone = payload.get("sub")
    user = get_user_by_phone(user_phone)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    ride = create_ride(user.id, data.pickup_location, data.drop_location)
    return {"ride_id": ride.id, "status": ride.status}

@router.get("/driver/pending-rides")
def list_pending_rides():
    return get_pending_rides()

@router.post("/driver/accept-ride")
def accept(ride: RideAccept, token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    phone = payload.get("sub")
    driver = login_driver(phone, "")  # using login to fetch driver
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    result = accept_ride(ride.ride_id, driver.id)
    if result:
        return {"message": "Ride accepted", "ride": result.id}
    raise HTTPException(status_code=400, detail="Ride not available")

@router.post("/ride/status-update")
def status_change(data: RideStatusUpdate):
    updated = update_ride_status(data.ride_id, data.status)
    if updated:
        return {"message": f"Ride updated to {data.status}"}
    raise HTTPException(status_code=404, detail="Ride not found")
