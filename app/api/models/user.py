import bcrypt
import re
from pydantic import BaseModel, validator, EmailStr
# write normal password schema


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator('password')
    def check_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password length must be at least 8 characters")
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least 1 uppercase letter")
        if not any(char.islower() for char in v):
            raise ValueError("Password must contain at least 1 lowercase letter")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least 1 digit")
        if not re.search(r"[!@#$%^&*()-_+=<>,.?/:;]", v):
            raise ValueError("Password must contain at least 1 punctuation mark")
        return v


class UserLogin(BaseModel):
    username: str
    password: str


class UserFromDB(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str

    def set_password(self, password: str):
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw((password.encode('utf-8'), self.hashed_password.encode('utf-8')))
