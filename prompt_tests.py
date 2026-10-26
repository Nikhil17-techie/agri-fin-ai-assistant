import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API configuration from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

client = genai.Client(api_key=API_KEY)

# Same question for all three experiments
test_question = (
    "My tomato plants have yellow leaves and slow growth. "
    "What could be the reasons, and what should I do first?"
)

prompts = {
    "Experiment 1 - Zero-shot": f"""
Answer the following question clearly and simply.

Question: {test_question}
""",

    "Experiment 2 - Role-based": f"""
You are an agricultural guidance assistant.

Explain possible causes of the problem and suggest practical
first steps using simple language. Do not claim a definite
diagnosis without sufficient information.

Question: {test_question}
""",

    "Experiment 3 - Structured": f"""
ROLE:
You are a responsible agricultural guidance assistant.

TASK:
Explain possible causes of yellow leaves and slow growth
in tomato plants.

INSTRUCTIONS:
- Use simple language.
- Explain multiple possible causes.
- Recommend practical, low-risk checks first.
- Do not claim a definite diagnosis without enough evidence.
- State what additional information would help.

OUTPUT FORMAT:
1. Summary
2. Possible causes
3. Recommended first steps
4. Important cautions
5. Additional information needed

USER QUESTION:
{test_question}
"""
}

for experiment_name, prompt in prompts.items():
    print("\n" + "=" * 65)
    print(experiment_name)
    print("=" * 65)

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.4,
                max_output_tokens=900,
            ),
        )

        print(response.text or "No text returned.")

    except Exception as error:
        print(f"Experiment failed: {error}")