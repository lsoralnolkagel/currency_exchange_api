from pydantic import BaseModel


class UserToRegister(BaseModel):
    username: str
    email: str
    full_name: str
    password: str


class UserInDB(BaseModel):
    username: str
    email: str
    full_name: str
    hashed_password: str

