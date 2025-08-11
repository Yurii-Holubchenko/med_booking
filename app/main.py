from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.core.request_limiter import limiter
from app.api.router import router
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.db import models
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical Appointment Booking")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.include_router(router)
