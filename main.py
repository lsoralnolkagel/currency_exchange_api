import uvicorn
from fastapi import FastAPI

from CEA.app.api.endpoints.users import user_router

app = FastAPI()


@app.get("/")
async def get_main():
    return {"message": "Welcome to the Currency Exchange Rates API server"}

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
