import jwt
import os
import json
from datetime import datetime, timedelta, timezone
from cryptography.fernet import Fernet

class AccessTokenEncryptor:
    def __init__(self):
        self.jwt_secret = os.getenv("JWT_SECRET_KEY")
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM")

        fernet_jwt_key = os.getenv("FERNET_JWT_KEY")
        self.fernet = Fernet(fernet_jwt_key.encode())

    # Generate JWT token
    def generate(self, payload: dict[str, int]) -> str:
        jwt_payload = {
            "data": self.__encrypted_payload(payload),
            "expiration": self.__expiration()
        }

        jwt_token = jwt.encode(jwt_payload, self.jwt_secret, algorithm=self.jwt_algorithm)

        return jwt_token

    # Parse JWT token
    def parse(self, jwt_token: str) -> dict:
        decode_token = jwt.decode(jwt_token, self.jwt_secret, algorithms=[self.jwt_algorithm])
        encrypted_data = decode_token["data"]
        decrypted_json = self.fernet.decrypt(encrypted_data.encode())

        return json.loads(decrypted_json.decode())

    def __expiration(self):
        """
        Add an expiration timestamp to the payload to make the access token value mutable.
        Otherwise, the access token will have a static value.
        """
        current_time = datetime.now(timezone.utc)
        time_delta = timedelta(minutes=15)
        expiration_time = int((current_time + time_delta).timestamp())

        return expiration_time

    def __encrypted_payload(self, payload):
        json_payload = json.dumps(payload).encode()
        encrypted_json_payload = self.fernet.encrypt(json_payload)

        return encrypted_json_payload.decode()
