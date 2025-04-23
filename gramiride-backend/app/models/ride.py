from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.services.database import Base
import enum

class RideStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    ongoing = "ongoing"
    completed = "completed"
    cancelled = "cancelled"

class Ride(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)
    pickup_location = Column(String)
    drop_location = Column(String)
    status = Column(Enum(RideStatus), default=RideStatus.pending)

    user = relationship("User")
    driver = relationship("Driver")
