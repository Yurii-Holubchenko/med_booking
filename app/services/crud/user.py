from typing import Optional
from sqlalchemy.orm import Session
from app.db.models.user import User
from datetime import datetime

async def find_user_by_id(user_id: int, db: Session) -> Optional[User]:
    return db.query(User).filter_by(id=user_id).first()

async def find_user_by_email(email: str, db: Session) -> Optional[User]:
    return db.query(User).filter_by(email=email).first()

async def find_user_by_confirmation_token(token: str, db: Session) -> Optional[User]:
    return db.query(User).filter_by(confirmation_token=token).first()

async def find_user_by_refresh_token(token: str, db: Session) -> Optional[User]:
    return db.query(User).filter_by(refresh_token=token).first()

async def find_user_by_reset_password_token(token: str, db: Session) -> Optional[User]:
    return db.query(User).filter_by(reset_password_token=token).first()

async def create_user(email: str, encrypted_password: str, token: str, expired_at: datetime, db: Session) -> User:
    user = User(
        email=email,
        encrypted_password=encrypted_password,
        confirmation_token=token,
        confirmation_token_expired_at=expired_at
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

async def set_refresh_token(user: User, token: str, expired_at: datetime, db: Session) -> None:
    user.refresh_token = token
    user.refresh_token_expired_at = expired_at
    db.add(user)
    db.commit()
    db.refresh(user)

async def set_reset_password_token(user: User, token: str, expired_at: datetime, db: Session) -> None:
    user.reset_password_token = token
    user.reset_password_token_expired_at = expired_at
    db.add(user)
    db.commit()
    db.refresh(user)

async def set_new_password(user: User, encrypted_password: str, db: Session) -> None:
    user.encrypted_password = encrypted_password
    user.reset_password_token = None
    user.reset_password_token_expired_at = None
    db.add(user)
    db.commit()
    db.refresh(user)

async def reset_confirmation_token(user: User, db: Session) -> None:
    user.confirmation_token = None
    user.confirmation_token_expired_at = None
    db.commit()
    db.refresh(user)

async def reset_refresh_token(user: User, db: Session) -> None:
    user.refresh_token = None
    user.refresh_token_expired_at = None
    db.add(user)
    db.commit()
    db.refresh(user)
