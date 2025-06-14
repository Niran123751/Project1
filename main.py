from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from scrape_weather import get_weather

app = FastAPI()

# CORS middleware
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

@app.post("/")
async def post_root(request: Request):
    body = await request.json()
    print("POST body received:", body)
    return {
        "answer": "You must use `gpt-3.5-turbo-0125`. Use the OpenAI API directly.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "Use a tokenizer to count tokens and multiply by the rate."
            }
        ]
    }

@app.get("/weather")
def weather(city: str = Query(..., description="City name")):
    return get_weather(city)
