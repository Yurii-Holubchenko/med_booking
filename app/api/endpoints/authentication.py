from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.services.auth.authentication import Authentication
from app.services.auth.registration import Registration
from app.services.auth.confirmation import Confirmation
from app.models.authentication import Login, LoginResponse
from app.db.database import db_connection

router = APIRouter(tags=["authentication"])

@router.post("/login", response_model=LoginResponse)
async def login(user: Login, db: Session = Depends(db_connection)):
    return await Authentication(user.email, user.password, db)()

@router.post("/registration")
async def registration(user: Login, background_tasks: BackgroundTasks, db: Session = Depends(db_connection)):
    return await Registration(user.email, user.password, background_tasks, db)()

@router.get("/confirmation")
async def confirmation(token: str, db: Session = Depends(db_connection)):
    return await Confirmation(token, db)()
