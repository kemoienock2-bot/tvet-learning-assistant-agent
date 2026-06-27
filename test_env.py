import os
from dotenv import load_dotenv

loaded = load_dotenv()

print("Loaded:", loaded)
print("API Key:", os.getenv("GEMINI_API_KEY"))