import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from CEA.app.api.models.user import UserInDB, UserToRegister
from CEA.app.api.db.database import get_db
from CEA.app.api.db.models import User
from CEA.app.core.security import authenticate_user, create_access_token, get_current_user, get_password_hash


user_router = APIRouter(prefix="/auth")
security = HTTPBasic()


@user_router.post("/register/")
def register_user(user: UserToRegister, db: Session = Depends(get_db)):
    db_user = User(username=user.username, full_name=user.full_name, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"user created": db_user}



#@user_router.post("/login/")

