from fastapi import APIRouter
from app.services.auth.user_authentication import UserAuthentication
from app.models.login import Login

router = APIRouter(tags=["authentication"])

@router.post("/login")
async def login(user: Login):
  return UserAuthentication(user.email, user.password).__call__()
