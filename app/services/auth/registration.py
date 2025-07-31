from typing import Union
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.crud.user import find_user_by_email, create_user
from app.core.security import encrypt_password
from app.db.models.user import User
from app.services.auth.confirmation_token_encryptor import ConfirmationTokenEncryptor

class Registration:
    def __init__(self, email: str, password: str, db: Session):
        self.email = email
        self.password = password
        self.db = db

    async def __call__(self) -> Union[User, HTTPException]:
        user = await find_user_by_email(self.email, self.db)

        if user:
            raise HTTPException(status_code=401, detail=f"User with email {self.email} already exists")

        confirmation_token, confirmation_token_expired_at = ConfirmationTokenEncryptor(self.email).generate()

        user = await create_user(
            self.email,
            encrypt_password(self.password),
            confirmation_token,
            confirmation_token_expired_at,
            self.db
        )

        return user
