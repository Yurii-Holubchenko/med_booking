from sqlalchemy.orm import Session

class Confirmation:
    def __init__(self, token: str, db: Session):
        self.token = token
        self.db = db

    async def __call__(self):
        pass
