"""import requests
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from CEA.app.api.endpoints.users import authenticate_user, get_user
from CEA.app.api.models.user import UserLogin

currency_router = APIRouter(prefix="/currency")
security = HTTPBasic()


def validate_user(user: HTTPBasicCredentials = Depends(security)):
    return authenticate_user(user.username, user.password)


@currency_router.get("/all/")
async def get_all_currency_list(user: UserLogin = Depends(validate_user)):
    if authenticate_user(get_user(user.username)):
        url = "https://api.apilayer.com/currency_data/list"
        payload = {}
        headers = {"apikey": "th9mwKy6fXqwWd3gubGvgiaa7REE9zDI"}
        response = requests.request("GET", url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.text
        return {status_code: result}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")"""