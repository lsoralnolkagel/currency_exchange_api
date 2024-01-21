import uvicorn
from fastapi import FastAPI

# import routers

app = FastAPI()


@app.get("/")
async def get_main():
    return {"message": "Welcome to the Currency Exchange Rates API server"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
