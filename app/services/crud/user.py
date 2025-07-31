from typing import Optional
from sqlalchemy.orm import Session
from app.db.models.user import User
from datetime import datetime

async def find_user_by_email(email: str, db: Session) -> Optional[User]:
    user = db.query(User).filter_by(email=email).first()

    return user

async def update_refresh_token(user: User, refresh_token: str, expired_at: datetime, db: Session) -> None:
    user.refresh_token = refresh_token
    user.refresh_token_expired_at = expired_at
    db.add(user)
    db.commit()

async def create_user(email: str, encrypted_password: str, confirmation_token: str, confirmation_token_expired_at: datetime, db: Session) -> User:
    user = User(
        email=email,
        encrypted_password=encrypted_password,
        confirmation_token=confirmation_token,
        confirmation_token_expired_at=confirmation_token_expired_at
    )
    db.add(user)
    db.commit()

    return user
