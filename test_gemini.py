from utils.gemini_helper import get_gemini_client


client = get_gemini_client()

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say hello."
    )
    print(response.text)
except Exception as e:
    print("ERROR:", type(e).__name__)
    print(e)