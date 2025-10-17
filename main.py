from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import requests
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
STACK = os.getenv("STACK")

# Try to handle root path
@app.get("/")
def root():
    return RedirectResponse(url="/me")

# Profile endpoint with rate limiting
@app.get("/me")
@limiter.limit("10/minute")
def get_profile(request: Request):

    try:
        # Fetch cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Could not retrieve cat fact.")
    except Exception:
        cat_fact = "Cat API is currently unavailable. Please try again later."

    return {
        "status": "success",
        "user": {
            "email": EMAIL,
            "name": NAME,
            "stack": STACK
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }
