import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-3.8-flash"
)


def classify_document(text):

    text = text[:8000]

    prompt = f"""
Classify this document into one of the following categories:

- SRS
- Design Document
- Technical Report
- User Manual
- Test Plan
- Research Paper

Return only the category name.

Document:

{text}
"""

    response = model.generate_content(prompt)

    return response.text.strip()
