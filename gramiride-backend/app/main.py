from fastapi import FastAPI
from app.routes import user
from app.routes import ws
from app.routes import user, driver
from app.routes import ride
from routes import feedback

app = FastAPI(title="GramiRide API")
app.include_router(ws.router)
app.include_router(user.router)
app.include_router(driver.router)


@app.get("/")
def root():
    return {"message": "Welcome to GramiRide!"}


app.include_router(ride.router)

app.include_router(feedback.router)

from routes import admin
app.include_router(admin.router)


