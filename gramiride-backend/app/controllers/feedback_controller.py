from sqlalchemy.orm import Session
from models.feedback import FeedbackCreate
from database import Feedback, Ride

def submit_feedback(db: Session, user_id: int, data: FeedbackCreate):
    ride = db.query(Ride).filter(Ride.id == data.ride_id).first()
    if not ride:
        return None
    feedback = Feedback(
        ride_id=data.ride_id,
        user_id=user_id,
        driver_id=ride.driver_id,
        rating=data.rating,
        comment=data.comment
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback
