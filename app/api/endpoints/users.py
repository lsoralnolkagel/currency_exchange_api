import jwt
from datetime import timedelta, datetime
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.sql import select
from CEA.app.api.models.user import UserCreate, UserLogin, UserFromDB
from CEA.app.api.db.database import get_async_session, async_session_maker
from CEA.app.api.db.models import User

user_router = APIRouter(prefix="/auth")

SECRET_KEY = "dba749b064fa8502475b7bd8b31b81d2cb20a34fbfee762ba4ba9c09093c799a"
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(hours=72)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def verify_password(entered_password, hashed_password):
    return pwd_context.verify(entered_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    with async_session_maker() as session:
        user = session.execute(select(User).where(User.username == username)).first()
        return user


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or not verify_password(password, user.password):
        return False
    return True


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=EXPIRATION_TIME)
    to_encode.update({"exp": expire})
    encoded_jwt =jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@user_router.post("/register/")
async def register_user(new_user: UserCreate):
    async with async_session_maker() as session:
        user = UserCreate(**new_user.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


@user_router.post("/login/")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    async with async_session_maker() as session:
        username = form_data.username
        password = form_data.password

        if not authenticate_user(username, password):
            raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})

        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}