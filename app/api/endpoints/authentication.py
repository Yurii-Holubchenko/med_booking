from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.core.request_limiter import limiter
from app.services.auth.authentication import Authentication
from app.services.auth.registration import Registration
from app.services.auth.confirmation import Confirmation
from app.services.auth.access_token_refresh import AccessTokenRefresh
from app.services.auth.logout import Logout
from app.models.authentication import Login, LoginResponse
from app.db.database import db_connection

router = APIRouter(tags=["authentication"])

@router.post("/registration")
@limiter.limit("3/minute") # Max 3 registration from one IP in a minute
async def registration(user: Login, request: Request, background_tasks: BackgroundTasks, db: Session = Depends(db_connection)):
    _ = request # Variable "request" needs only for slowapi
    return await Registration(user.email, user.password, background_tasks, db)()

@router.get("/confirmation")
async def confirmation(token: str, db: Session = Depends(db_connection)):
    return await Confirmation(token, db)()

@router.post("/login", response_model=LoginResponse)
async def login(user: Login, db: Session = Depends(db_connection)):
    return await Authentication(user.email, user.password, db)()

@router.post("/access_token_refresh")
async def access_token_refresh(refresh_token: str, db: Session = Depends(db_connection)):
    return await AccessTokenRefresh(refresh_token, db)()

@router.delete("/logout")
async def logout(access_token: str, db: Session = Depends(db_connection)):
    return await Logout(access_token, db)()
