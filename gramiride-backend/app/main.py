from fastapi import FastAPI
from app.routes import user

app = FastAPI(title="GramiRide API")

from app.routes import user, driver

app.include_router(user.router)
app.include_router(driver.router)

@app.get("/")
def root():
    return {"message": "Welcome to GramiRide!"}

from app.routes import ride
app.include_router(ride.router)
