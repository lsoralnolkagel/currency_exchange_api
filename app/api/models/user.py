import bcrypt
from pydantic import BaseModel, EmailStr, constr



class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8, pattern=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')


class UserFromDB(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str

    def set_password(self, password: str):
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw((password.encode('utf-8'), self.hashed_password.encode('utf-8'))
