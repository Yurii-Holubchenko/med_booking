from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.services.auth.user_authentication import UserAuthentication
from app.models.login import Login
from app.db.database import db_connection

router = APIRouter(tags=["authentication"])

@router.post("/login")
async def login(user: Login, db: Session = Depends(db_connection)):
  return await UserAuthentication(user.email, user.password, db)()
