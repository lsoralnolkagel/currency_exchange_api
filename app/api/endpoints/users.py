import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic,OAuth2PasswordRequestForm
from CEA.app.api.models.user import RegisterUser, UserInDB
from CEA.app.api.db.database import get_async_session, async_session_maker
from CEA.app.api.db.models import User
from CEA.app.core.security import authenticate_user, create_access_token, get_current_user


user_router = APIRouter(prefix="/auth")
security = HTTPBasic()


@user_router.post("/register/")
async def register_new_user(new_user: RegisterUser):
    async with get_async_session() as session:
        username = new_user.username.lower()
        existing_user = await session.query(User).filter(User.username == username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")

        user = User(username=new_user.username, email=new_user.email, hashed_password=new_user.hashed_password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user


@user_router.post("/login/")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
