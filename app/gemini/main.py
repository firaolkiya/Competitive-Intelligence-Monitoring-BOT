import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


def generate_text(prompt_text, client):
   
    try:
        response = client.models.generate_content(
             model="gemini-2.5-flash",
            contents=prompt_text,
         )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"


if __name__=="__main__":
    try:
        client = genai.Client(
            api_key=API_KEY
        )
        response = generate_text("Explain how AI works in a few words",client=client)
        print(response)

    except KeyError:
        print("Please set the GOOGLE_API_KEY environment variable or hardcode it in the script.")
        exit()
