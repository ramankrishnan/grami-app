# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String, default="user")  # ← NEW
    is_active = Column(Boolean, default=True)  # ← NEW

# Driver model
class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True)
    is_active = Column(Boolean, default=True)  # ← NEW
