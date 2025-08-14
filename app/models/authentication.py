from pydantic import BaseModel, EmailStr, ConfigDict, Field

class LoginParams(BaseModel):
    email: EmailStr
    password: str

    # __pydantic_extra__: dict[str, str] = Field(init=False)

    # *extra* - Allow extra attributes for model. Possible values: "ignore"(default), "allow", "forbid"
    # model_config = ConfigDict(extra="allow")

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str

class ResetPasswordConfirmationParams(BaseModel):
    token: str
    password: str
    new_password: str
