from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, User, Driver, Ride, Feedback
from auth.admin_checker import admin_required

router = APIRouter()

@router.get("/admin/users")
def list_users(db: Session = Depends(get_db), admin = Depends(admin_required)):
    return db.query(User).all()

@router.get("/admin/drivers")
def list_drivers(db: Session = Depends(get_db), admin = Depends(admin_required)):
    return db.query(Driver).all()

@router.get("/admin/rides")
def list_rides(db: Session = Depends(get_db), admin = Depends(admin_required)):
    return db.query(Ride).all()

@router.get("/admin/feedbacks")
def list_feedbacks(db: Session = Depends(get_db), admin = Depends(admin_required)):
    return db.query(Feedback).all()

@router.post("/admin/user/{user_id}/ban")
def ban_user(user_id: int, db: Session = Depends(get_db), admin = Depends(admin_required)):
    user = db.query(User).get(user_id)
    user.is_active = False
    db.commit()
    return {"status": "User banned"}

@router.post("/admin/driver/{driver_id}/ban")
def ban_driver(driver_id: int, db: Session = Depends(get_db), admin = Depends(admin_required)):
    driver = db.query(Driver).get(driver_id)
    driver.is_active = False
    db.commit()
    return {"status": "Driver banned"}

@router.post("/admin/user/{user_id}/unban")
def unban_user(user_id: int, db: Session = Depends(get_db), admin = Depends(admin_required)):
    user = db.query(User).get(user_id)
    user.is_active = True
    db.commit()
    return {"status": "User unbanned"}

@router.post("/admin/driver/{driver_id}/unban")
def unban_driver(driver_id: int, db: Session = Depends(get_db), admin = Depends(admin_required)):
    driver = db.query(Driver).get(driver_id)
    driver.is_active = True
    db.commit()
    return {"status": "Driver unbanned"}
