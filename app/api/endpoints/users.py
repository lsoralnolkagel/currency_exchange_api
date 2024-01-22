from fastapi import APIRouter
from CEA.app.api.models.user import UserCreate, UserFromDB

user_router = APIRouter(prefix="/auth/")

@user_router.post("/register/")
async def register_user(new_user: UserCreate):
    
@user_router.post("/login/")