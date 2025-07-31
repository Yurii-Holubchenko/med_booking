from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    encrypted_password = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    refresh_token_expired_at = Column(DateTime(timezone=True), nullable=True)
    confirmation_token = Column(String, nullable=True)
    confirmation_token_expired_at = Column(DateTime(timezone=True), nullable=True)
