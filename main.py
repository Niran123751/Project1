from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from scrape_weather import get_weather

app = FastAPI()

# Add CORS middleware to allow public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing/submission
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Weather API!"}

@app.get("/weather")
def weather(city: str = Query(..., description="City name")):
    return get_weather(city)

