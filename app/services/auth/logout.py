from sqlalchemy.orm import Session
from app.services.crud.user import reset_refresh_token
from app.core.access_token_finder import find_user_by_access_token

class Logout:
    def __init__(self, access_token: str, db: Session):
        self.access_token = access_token
        self.db = db

    async def __call__(self) -> dict[str, str]:
        user = await find_user_by_access_token(self.access_token, self.db)
        await reset_refresh_token(user, self.db)

        return {"message": "You have been successfully logged out"}
