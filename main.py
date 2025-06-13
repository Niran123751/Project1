from fastapi import FastAPI, Query
from scrape_weather import get_weather

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Weather API"}

@app.get("/weather")
def weather(city: str = Query(..., description="City name")):
    return get_weather(city)
