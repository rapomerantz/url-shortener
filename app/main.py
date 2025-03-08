from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import hashlib
import redis
import os
from redis_client import redis_client

# Initialize FastAPI app
app = FastAPI()

# # Initialize Redis connection
# redis_client = redis.Redis(
#     host=os.getenv("REDIS_HOST", "redis"),
#     port=int(os.getenv("REDIS_PORT", 6379)),
#     decode_responses=True
# )

class URLRequest(BaseModel):
    url: HttpUrl

class URLShortenerService:
    @staticmethod
    def generate_short_code(url: str) -> str:
        return hashlib.md5(url.encode()).hexdigest()[:6]

    @staticmethod
    def shorten_url(url: str) -> str:
        # Check if URL already has a short code
        existing_code = redis_client.get(url)
        if existing_code:
            return existing_code

        # Generate a new short code
        short_code = URLShortenerService.generate_short_code(url)

        # Store both short_code -> URL and URL -> short_code mappings
        redis_client.set(short_code, url)
        redis_client.set(url, short_code)  # Avoid duplicate short codes

        return short_code

    @staticmethod
    def get_original_url(short_code: str) -> str :
        return redis_client.get(short_code)

@app.get("/")
def root():
    return {"message": "Hello, in FastAPI"}

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = URLShortenerService.shorten_url(str(request.url))
    return {"original_url": request.url, "short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
def expand_url(short_code: str):
    original_url = URLShortenerService.get_original_url(short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"original_url": original_url}