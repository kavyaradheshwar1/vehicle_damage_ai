import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_ai_report(data):
    prompt = f"""
    Generate a professional vehicle damage inspection report based on:

    {data}

    Keep it clear and professional.
    """

    response = model.generate_content(prompt)
    return response.text