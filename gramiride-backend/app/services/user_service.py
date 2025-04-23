from sqlalchemy.orm import Session
from app.models.user import User
from app.services.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def register_user(name: str, phone: str, password: str):
    db: Session = SessionLocal()
    existing = db.query(User).filter(User.phone == phone).first()
    if existing:
        return False
    user = User(name=name, phone=phone, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return True
