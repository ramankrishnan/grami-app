from sqlalchemy.orm import Session
from app.models.ride import Ride, RideStatus
from app.services.database import SessionLocal

def create_ride(user_id: int, pickup: str, drop: str):
    db: Session = SessionLocal()
    ride = Ride(
        user_id=user_id,
        pickup_location=pickup,
        drop_location=drop,
        status=RideStatus.pending
    )
    db.add(ride)
    db.commit()
    db.refresh(ride)
    return ride

def get_pending_rides():
    db: Session = SessionLocal()
    return db.query(Ride).filter(Ride.status == RideStatus.pending).all()

def accept_ride(ride_id: int, driver_id: int):
    db: Session = SessionLocal()
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if ride and ride.status == RideStatus.pending:
        ride.driver_id = driver_id
        ride.status = RideStatus.accepted
        db.commit()
        return ride
    return None

def update_ride_status(ride_id: int, status: str):
    db: Session = SessionLocal()
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if ride:
        ride.status = status
        db.commit()
        return ride
    return None
