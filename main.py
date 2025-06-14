from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from scrape_weather import get_weather

app = FastAPI()

# CORS middleware for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_root():
    return {"message": "Welcome to the Weather API!"}

# Accept POST requests with JSON
@app.post("/")
async def post_root(request: Request):
    body = await request.json()
    print("POST body received:", body)
    return {"answer": "This is a dummy response for POST testing."}

@app.get("/weather")
def weather(city: str = Query(..., description="City name")):
    return get_weather(city)

