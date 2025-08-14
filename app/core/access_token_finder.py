from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.user import User
from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.crud.user import find_user_by_id

async def find_user_by_access_token(access_token: str, db: Session) -> User:
    try:
        user_dict = AccessTokenEncryptor().parse(access_token)
    except:
        raise HTTPException(status_code=400, detail="Access token is incorrect")

    if not user_dict or not user_dict["user_id"]:
        raise HTTPException(status_code=400, detail="Access token is incorrect")

    user = await find_user_by_id(user_dict["user_id"], db)

    if not user:
        raise HTTPException(status_code=400, detail="Access token is incorrect")

    return user
