from fastapi import APIRouter
from app.services.user_authentication import UserAuthentication

router = APIRouter(tags=["authentication"])

@router.post("/login")
async def login(email: str, password: str):
  return UserAuthentication(email, password).__call__()
