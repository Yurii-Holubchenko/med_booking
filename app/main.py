from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from app.api.router import router

from app.db import models
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical Appointment Booking")
app.include_router(router)
