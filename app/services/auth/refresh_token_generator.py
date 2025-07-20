import uuid, hashlib

from datetime import datetime, timedelta, timezone
from app.db.models.user import User
from sqlalchemy.orm import Session

class RefreshTokenGenerator:
    def __init__(self, user: User, db: Session):
        self.user = user
        self.db = db

    def generate(self) -> str:
        refresh_token = str(uuid.uuid4())

        hashed_refresh_token = hashlib.sha256(refresh_token.encode()).hexdigest()

        current_time = datetime.now(timezone.utc)
        time_delta = timedelta(days=30)
        refresh_token_expired_at = current_time + time_delta

        self.user.refresh_token = hashed_refresh_token
        self.user.refresh_token_expired_at = refresh_token_expired_at
        self.db.add(self.user)
        self.db.commit()

        return refresh_token
