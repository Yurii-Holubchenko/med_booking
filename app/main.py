from fastapi import FastAPI
from app.api.router import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Medical Appointment Booking")

app.include_router(router)
