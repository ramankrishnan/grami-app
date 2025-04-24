from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal, get_user_by_phone
from auth.auth_handler import get_password_hash
from database import User

# Create all tables (if not already created)
Base.metadata.create_all(bind=engine)

# Start DB session
db: Session = SessionLocal()

# Check if admin already exists
existing_admin = db.query(User).filter(User.phone == "9999999999").first()

if not existing_admin:
    admin = User(
        name="Admin",
        phone="9999999999",
        hashed_password=get_password_hash("adminpass"),
        is_active=True,
        role="admin"
    )
    db.add(admin)
    db.commit()
    print("✅ Admin user created.")
else:
    print("ℹ️ Admin already exists.")

db.close()
