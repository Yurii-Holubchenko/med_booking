from typing import Optional

from sqlalchemy.orm import Session

from app.db.models.user import User

async def find_user_by_email(email: str, db: Session) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()

    return user
