import uuid, hashlib

from datetime import datetime, timedelta, timezone
from app.db.models.user import User
from sqlalchemy.orm import Session
from app.services.crud.user import update_refresh_token

class RefreshTokenEncryptor:
    def __init__(self, user: User, db: Session):
        self.user = user
        self.db = db

    async def generate(self) -> str:
        token = str(uuid.uuid4())
        hashed_token = hashlib.sha256(token.encode()).hexdigest()
        token_expired_at = datetime.now(timezone.utc) + timedelta(days=30)

        await update_refresh_token(self.user, hashed_token, token_expired_at, self.db)

        return token
