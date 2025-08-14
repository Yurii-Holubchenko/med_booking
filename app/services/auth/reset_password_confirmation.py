from sqlalchemy.orm import Session

class ResetPasswordConfirmation:
    def __init__(self, token: str, password: str, new_password: str, db: Session):
        self.token = token
        self.password = password
        self.new_password = new_password
        self.db = db

    async def __call__(self) -> dict[str, str]:
        # Find user by token
        # verify_password for user
        # set new password and reset reset_password + reset_password_token_expired_at
        return {"message": f"Password was reset successfully"}
