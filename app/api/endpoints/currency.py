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


@currency_router.get("/list/")
def get_all_currency_list(user: UserToLogin = Depends(validate_user)):
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


@currency_router.get("/exchange/")
def get_exchange_courses(from_c: str, to_c: str, amount: int, user: UserToLogin = Depends(validate_user)):
    all_codes = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD",
                 "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP",
                 "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC",
                 "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD",
                 "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL",
                 "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD",
                 "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK",
                 "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK",
                 "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO",
                 "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR",
                 "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE",
                 "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP",
                 "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VES", "VND",
                 "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    if from_c.upper() not in all_codes or to_c.upper() not in all_codes:
        raise HTTPException(status_code=400, detail="Incorrect currency code(s)")
    else:
        if user:
            url = f"https://api.apilayer.com/currency_data/convert?to={to_c.upper()}&from={from_c.upper()}&amount={amount}"

            payload = {}
            headers = {"apikey": "th9mwKy6fXqwWd3gubGvgiaa7REE9zDI"}

            response = requests.request("GET", url, headers=headers, data=payload)

            status_code = response.status_code
            result = response.text
            if status_code == 200:
                data = json.loads(result)
                currencies = str(data.get("result"))
                return Response(content=currencies, media_type="text/plain")
            else:
                raise HTTPException(status_code=500, detail="Failed to exchange currency. Invalid code")
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")