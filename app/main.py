from gemini.main import generate_text
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if __name__=="Main":
    client = genai.Client(
            api_key=API_KEY
        )
