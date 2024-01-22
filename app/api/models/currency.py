from pydantic import BaseModel


class CurrencyToExchange(BaseModel):
    currency_code_in: int
    currency_code_out: int
    quantity: float = 1


class CurrencyExchanged(BaseModel):
    currency_code_out: int
    quantity: float
