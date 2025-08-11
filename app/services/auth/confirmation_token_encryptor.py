import uuid, hashlib

from datetime import datetime, timedelta, timezone

class ConfirmationTokenEncryptor:
    def __init__(self, email: str, expires_in_hours: int = 24):
        self.email = email
        self.expires_in_hours = expires_in_hours

    def generate(self) -> tuple[str, datetime]:
        salt = uuid.uuid4().hex
        raw_token = f"{self.email}{salt}".encode()
        hashed_token = hashlib.sha256(raw_token).hexdigest()
        token_expired_at = datetime.now(timezone.utc) + timedelta(hours=self.expires_in_hours)

        return hashed_token, token_expired_at
