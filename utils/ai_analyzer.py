import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_image(image):
    prompt = """
    Analyze this vehicle image and return ONLY valid JSON.
    Do NOT include markdown or backticks.

    {
        "damage_type": "",
        "severity": "",
        "estimated_cost": "",
        "explanation": ""
    }
    """

    response = model.generate_content([prompt, image])
    text = response.text

    # 🔥 Remove ```json ... ```
    cleaned = re.sub(r"```json|```", "", text).strip()

    try:
        return json.loads(cleaned)
    except:
        return {"error": cleaned}