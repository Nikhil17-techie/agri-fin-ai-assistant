
import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key not found in .env")
    raise SystemExit

try:
    client = genai.Client(api_key=api_key)

    print("Testing gemini-3.8-flash...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Reply with: My Agriculture Assistant is working."
    )

    print("\nSUCCESS!")
    print(response.text)

except Exception as error:
    print("\nTEST FAILED:")
    print(error)

