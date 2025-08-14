from fastapi import HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.services.crud.user import find_user_by_email, set_reset_password_token
from app.services.mailers.registration import send_password_reset_email
from app.services.auth.reset_password_token_encryptor import ResetPasswordTokenEncryptor

class ResetPassword:
    def __init__(self, email: str, background_tasks: BackgroundTasks, db: Session):
        self.email = email
        self.db = db
        self.background_tasks = background_tasks

    async def __call__(self) -> dict[str, str]:
        user = await find_user_by_email(self.email, self.db)

        if not user:
            raise HTTPException(status_code=401, detail=f"User with email {self.email} doesn't exist")

        token, token_expired_at = ResetPasswordTokenEncryptor(self.email).generate()
        await set_reset_password_token(user, token, token_expired_at, self.db)

        self.background_tasks.add_task(send_password_reset_email, user.email, token)

        return {"message": f"Email with password reset information was sent to {user.email}"}
