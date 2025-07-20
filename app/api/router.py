from fastapi import APIRouter
from app.api.endpoints import authentication

router = APIRouter()

router.include_router(authentication.router)
