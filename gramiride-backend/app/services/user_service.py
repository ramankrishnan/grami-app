from sqlalchemy.orm import Session
from app.models.user import User
from app.services.database import SessionLocal, engine, Base
from app.services.auth import hash_password, verify_password

Base.metadata.create_all(bind=engine)

def register_user(name: str, phone: str, password: str):
    db: Session = SessionLocal()
    existing = db.query(User).filter(User.phone == phone).first()
    if existing:
        return False
    user = User(name=name, phone=phone, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return True

def login_user(phone: str, password: str):
    db: Session = SessionLocal()
    user = db.query(User).filter(User.phone == phone).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

