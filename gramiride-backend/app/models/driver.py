from sqlalchemy import Column, Integer, String
from app.services.database import Base

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True)
    vehicle_number = Column(String)
    vehicle_type = Column(String)
    hashed_password = Column(String)
