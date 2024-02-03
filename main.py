import uvicorn
from fastapi import FastAPI

from CEA.app.api.endpoints.users import user_router
#from CEA.app.api.endpoints.currency import currency_router

app = FastAPI()


@app.get("/")
async def get_main():
    return {"message": "Welcome to the Currency Exchange Rates API server"}

app.include_router(user_router)
#app.include_router(currency_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
