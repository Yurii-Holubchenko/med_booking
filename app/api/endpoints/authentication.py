from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.services.auth.authentication import Authentication
from app.services.auth.registration import Registration
from app.services.auth.confirmation import Confirmation
from app.models.authentication import Login, LoginResponse, RegistrationResponse
from app.db.database import db_connection

router = APIRouter(tags=["authentication"])

@router.post("/login", response_model=LoginResponse)
# We can send parameter db, for example in tests
async def login(user: Login, db: Session = Depends(db_connection)):
    return await Authentication(user.email, user.password, db)()

@router.post("/registration", response_model=RegistrationResponse)
async def registration(user: Login, db: Session = Depends(db_connection)):
    return await Registration(user.email, user.password, db)()

@router.get("/confirmation")
async def confirmation(token: str, db: Session = Depends(db_connection)):
    return await Confirmation(token, db)()
