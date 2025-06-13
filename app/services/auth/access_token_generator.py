import jwt
import os
from datetime import datetime, timedelta, timezone

class AccessTokenGenerator:
  def __init__(self, payload: dict):
    self.payload = payload

  def generate(self):
    self.add_expiration()

    secret = os.getenv("JWT_SECRET_KEY")
    algorithm = os.getenv("JWT_ALGORITHM")
    jwt_token = jwt.encode(self.payload, secret, algorithm=algorithm)

    return jwt_token

  def add_expiration(self):
    """
    Add an expiration timestamp to the payload to make the access token value mutable.
    Otherwise, the access token will have a static value.
    """
    current = datetime.now(timezone.utc)
    delta = timedelta(minutes=15)
    expiration_time = int((current + delta).timestamp())

    self.payload.update({"expiration": expiration_time})
