from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.auth.refresh_token_generator import RefreshTokenGenerator

class UserAuthentication:
  def __init__(self, email: str, password: str):
    self.email = email
    self.password = password

  def __call__(self):
    # User validation
    user_id = 111

    # Access token generation
    payload = {"user_id": user_id}
    access_token = AccessTokenEncryptor().generate(payload)

    # For future decryption
    # print(AccessTokenEncryptor().parse(access_token))

    # Refresh token generation
    refresh_token = RefreshTokenGenerator(user_id).generate()

    return {
      "access_token": access_token,
      "refresh_token": refresh_token
    }
