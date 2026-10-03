import os

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-3.8-flash"
)


def summarize_document(text):

    text = text[:15000]

    prompt = f"""

    Summarize this engineering document.

    Include:

    1. Executive Summary
    2. Key Requirements
    3. Technologies Used
    4. Risks

    Document:

    {text}

    """

    response = model.generate_content(
        prompt
    )

    return response.text