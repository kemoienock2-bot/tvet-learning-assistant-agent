import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)


def get_gemini_client(retries: int = 3, backoff: float = 1.0) -> genai.Client:
    """Create and return a Gemini client, retrying on transient failures."""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(f"GEMINI_API_KEY not found in {ENV_PATH}")

    for attempt in range(1, retries + 1):
        try:
            return genai.Client(api_key=api_key)
        except Exception as exc:
            if attempt == retries:
                raise
            time.sleep(backoff * attempt)


def generate_gemini_response(prompt: str, model: str = "gemini-2.5-flash", retries: int = 3, backoff: float = 1.0) -> str:
    """Generate text from Gemini with retry logic for temporary API errors."""

    client = get_gemini_client()

    for attempt in range(1, retries + 1):
        try:
            response = client.models.generate_content(model=model, contents=prompt)
            if hasattr(response, "text") and response.text:
                return response.text
            return str(response)
        except Exception as exc:
            exception_message = str(exc).lower()
            transient = "503" in exception_message or "service unavailable" in exception_message
            if attempt == retries or not transient:
                raise
            time.sleep(backoff * attempt)

    raise RuntimeError("Gemini request failed after retries.")
