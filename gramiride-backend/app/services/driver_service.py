from sqlalchemy.orm import Session
from app.models.driver import Driver
from app.services.database import SessionLocal, engine, Base
from app.services.auth import hash_password, verify_password

Base.metadata.create_all(bind=engine)

def register_driver(name: str, phone: str, vehicle_number: str, vehicle_type: str, password: str):
    db: Session = SessionLocal()
    existing = db.query(Driver).filter(Driver.phone == phone).first()
    if existing:
        return False
    driver = Driver(
        name=name,
        phone=phone,
        vehicle_number=vehicle_number,
        vehicle_type=vehicle_type,
        hashed_password=hash_password(password)
    )
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return True

def login_driver(phone: str, password: str):
    db: Session = SessionLocal()
    driver = db.query(Driver).filter(Driver.phone == phone).first()
    if not driver or not verify_password(password, driver.hashed_password):
        return None
    return driver
