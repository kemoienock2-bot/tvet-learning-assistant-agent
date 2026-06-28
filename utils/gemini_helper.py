import os
import time
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


def _load_local_env() -> None:
    """Load environment variables from the local .env file."""
    load_dotenv(ENV_PATH)


def _get_api_key() -> str:
    """Return the Gemini API key from Streamlit Secrets or local .env."""
    api_key = st.secrets.get("GEMINI_API_KEY")
    if api_key:
        return api_key

    if not os.getenv("GEMINI_API_KEY"):
        _load_local_env()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in Streamlit Secrets or local .env file. "
            "Set the key in Streamlit Secrets for Cloud deployment or in .env for local development."
        )

    return api_key


def get_gemini_client(retries: int = 3, backoff: float = 1.0) -> genai.Client:
    """Create and return a configured Gemini client with retry logic."""
    api_key = _get_api_key()

    for attempt in range(1, retries + 1):
        try:
            return genai.Client(api_key=api_key)
        except Exception as exc:
            if attempt == retries:
                raise
            time.sleep(backoff * attempt)
