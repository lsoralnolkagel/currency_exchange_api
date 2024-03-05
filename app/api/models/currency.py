from pydantic import BaseModel


class CurrencyToExchange(BaseModel):
    currency_code_in: str
    currency_code_out: str
    quantity: float = 1


class CurrencyExchanged(BaseModel):
    currency_code_out: str
    quantity: float
