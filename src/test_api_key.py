import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key loaded successfully ✅")
else:
    print("API key NOT found ❌")
