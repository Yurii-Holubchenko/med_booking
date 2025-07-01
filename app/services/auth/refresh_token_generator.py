import uuid
import hashlib

class RefreshTokenGenerator:
  def __init__(self, user_id: int):
    self.user_id = user_id

  def generate(self) -> str:
    refresh_token = str(uuid.uuid4())

    # For store in DB
    hashed_refresh_token = hashlib.sha256(refresh_token.encode()).hexdigest()

    return refresh_token
