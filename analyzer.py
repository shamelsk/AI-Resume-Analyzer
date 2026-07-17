import json
import os

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text):

    prompt = f"""
{SYSTEM_PROMPT}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    cleaned_response = response.text.strip()

    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response.replace("```json", "").replace("```", "").strip()

    elif cleaned_response.startswith("```"):
        cleaned_response = cleaned_response.replace("```", "").strip()

    return json.loads(cleaned_response)
