from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Union
from jwt.exceptions import InvalidSignatureError
from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.crud.user import find_user_by_id, reset_refresh_token

class Logout:
    def __init__(self, access_token: str, db: Session):
        self.access_token = access_token
        self.db = db

    async def __call__(self) -> Union[dict[str, str], HTTPException]:
        try:
            user_dict = AccessTokenEncryptor().parse(self.access_token)
        except InvalidSignatureError:
            raise HTTPException(status_code=400, detail="Access token is incorrect")

        if not user_dict or not user_dict["user_id"]:
            raise HTTPException(status_code=400, detail="Access token is incorrect")

        user = await find_user_by_id(user_dict["user_id"], self.db)

        if not user:
            raise HTTPException(status_code=400, detail="Access token is incorrect")

        await reset_refresh_token(user, self.db)

        return {"message": "You have been successfully logged out"}
