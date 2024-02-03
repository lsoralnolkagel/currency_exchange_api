import requests
import json
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from CEA.app.core.security import authenticate_user, get_user
from CEA.app.api.models.user import UserToLogin
from CEA.app.api.db.database import get_db

currency_router = APIRouter(prefix="/currency")
security = HTTPBasic()


def validate_user(user: HTTPBasicCredentials = Depends(security)):
    return authenticate_user(user.username, user.password)


@currency_router.get("/all/")
async def get_all_currency_list(user: UserToLogin = Depends(validate_user)):
    db = next(get_db())
    if user:
        url = "https://api.apilayer.com/currency_data/list"
        payload = {}
        headers = {"apikey": "th9mwKy6fXqwWd3gubGvgiaa7REE9zDI"}
        response = requests.request("GET", url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.text
        if status_code == 200:
            data = json.loads(result)
            currencies = data.get("currencies", {})
            formatted_currencies = "\n".join([f"{key}: {value}" for key, value in currencies.items()])
            return Response(content=formatted_currencies, media_type="text/plain")
        else:
            raise HTTPException(status_code=500, detail="Failed to fetch currency list")
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
