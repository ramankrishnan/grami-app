from fastapi import FastAPI
from app.routes import user

app = FastAPI(title="GramiRide API")

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to GramiRide!"}
