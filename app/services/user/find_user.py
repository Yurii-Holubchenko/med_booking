from sqlalchemy.orm import Session

from app.db.models.user import User

class FindUser:
  def __init__(self, email: str, password: str, db: Session):
    self.email = email
    self.password = password
    self.db = db

  async def __call__(self):
    user = self.db.query(User).filter(
      User.email == self.email,
      User.encrypted_password == self.password
    ).first()

    return user
