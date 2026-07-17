import os
import json
import time
import random

from json_schema import CURRICULUM_MAP_SCHEMA
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MODEL_NAME

# ----------------------------------------------------
# Load API Key
# ----------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

# ----------------------------------------------------
# Generate Curriculum
# ----------------------------------------------------

def generate_curriculum(prompt):

    MAX_RETRIES = 5

    for attempt in range(MAX_RETRIES):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,

                config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=8192,
                response_mime_type="application/json",
                ),
            )

            text = response.text.strip()

            # Remove markdown code fences if Gemini returns them
            if text.startswith("```json"):
                text = text.replace("```json", "", 1)

            if text.endswith("```"):
                text = text[:-3]

            text = text.strip()

            data = json.loads(text)

            return data

        except json.JSONDecodeError:

            return {
                "success": False,
                "error": "Gemini returned invalid JSON.",
                "raw_response": text,
            }

        except Exception as e:

            error = str(e)

            # Retry if Gemini is temporarily overloaded
            if "503" in error and attempt < MAX_RETRIES - 1:

                wait_time = (2 ** attempt) + random.uniform(0, 1)

                print(
                    f"Gemini busy. Retry {attempt + 1}/{MAX_RETRIES} in {wait_time:.1f} seconds..."
                )

                time.sleep(wait_time)

                continue

            return {
                "success": False,
                "error": error,
            }