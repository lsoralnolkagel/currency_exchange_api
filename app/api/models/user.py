from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class PyUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    # disabled: bool | None = None


class RegisterUser(PyUser):
    password: str


class UserInDB(PyUser):
    hashed_password: str
