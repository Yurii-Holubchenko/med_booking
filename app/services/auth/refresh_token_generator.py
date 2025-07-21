import uuid, hashlib

from datetime import datetime, timedelta, timezone
from app.db.models.user import User
from sqlalchemy.orm import Session
from app.services.crud.user import update_refresh_token

class RefreshTokenGenerator:
    def __init__(self, user: User, db: Session):
        self.user = user
        self.db = db

    async def generate(self) -> str:
        refresh_token = str(uuid.uuid4())

        hashed_refresh_token = hashlib.sha256(refresh_token.encode()).hexdigest()

        current_time = datetime.now(timezone.utc)
        time_delta = timedelta(days=30)
        refresh_token_expired_at = current_time + time_delta

        await update_refresh_token(self.user, hashed_refresh_token, refresh_token_expired_at, self.db)

        return refresh_token
