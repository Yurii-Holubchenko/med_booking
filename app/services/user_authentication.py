from app.services.access_token_generator import AccessTokenGenerator

class UserAuthentication:
  def __init__(self, email: str, password: str):
    self.email = email
    self.password = password

  def __call__(self):
    # User validation
    user_id = 111

    # Access token generation
    payload = {"user_id": user_id}
    access_token = AccessTokenGenerator(payload).generate()

    # Refresh token generation

    return {
      "access_token": access_token,
      "refresh_token": "ref_token"
    }
