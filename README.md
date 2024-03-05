
# Currency Exchange Project

This is a simple currency exchange Python project built using FastAPI with data stored in PostgreSQL database.

## Features
- Users can view current exchange rates for different currencies
- Users can convert one currency to another based on current exchange rates
- Users can sign up and log in to convert currency

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

## Setup
1. Clone the repository
2. Install the required dependencies by running pip install -r requirements.txt
3. Set up PostgreSQL database and update the database connection string in the code
4. Run the application by running uvicorn main:app --reload

## API Endpoints

- /currency/list - GET: Get all currency codes
- /currency/exchange/?from_c=USD&to_c=EUR&amount=100 - GET: Convert currency (example)
- /auth/register - POST: Create an account
- /auth/login - POST: Log into your account

## Future Improvements
- Add history of exchanges
- Improve error handling
