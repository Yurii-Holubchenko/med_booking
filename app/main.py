from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="Medical Appointment Booking")

app.include_router(router)
