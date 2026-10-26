import os
import time
from datetime import datetime

from dotenv import load_dotenv
from google import genai


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found. "
        "Please check your .env file."
    )

client = genai.Client(api_key=API_KEY)


# ============================================================
# EXPERIMENT QUESTION
# ============================================================

QUESTION = (
    "My tomato plants have yellow leaves and slow growth. "
    "What could be the reasons, and what should I do first?"
)


# ============================================================
# THREE PROMPTING TECHNIQUES
# ============================================================

PROMPTS = {
    "ZERO-SHOT PROMPTING": QUESTION,

    "ROLE-BASED PROMPTING": (
        "Act as an agricultural extension assistant who provides "
        "practical guidance to farmers.\n\n"
        f"Question: {QUESTION}\n\n"
        "Explain possible reasons for the problem and suggest "
        "practical first steps. Use simple language."
    ),

    "STRUCTURED PROMPTING": (
        "You are an agricultural guidance assistant.\n\n"
        "Task: Help the user understand the tomato plant problem "
        "and identify appropriate first steps.\n\n"
        f"Question: {QUESTION}\n\n"
        "Instructions:\n"
        "1. Explain possible causes without claiming a definite diagnosis.\n"
        "2. Recommend simple checks the user can perform first.\n"
        "3. Give practical next steps based on the observations.\n"
        "4. Include relevant precautions.\n"
        "5. Do not recommend unnecessary chemicals or excessive fertilizer.\n\n"
        "Use the following output format:\n\n"
        "Possible Causes:\n"
        "- List the possible causes.\n\n"
        "First Steps:\n"
        "- Explain what the user should check or do first.\n\n"
        "Precautions:\n"
        "- Mention important precautions.\n\n"
        "Follow-up Questions:\n"
        "- Ask for information that would help narrow down the cause."
    ),
}


# ============================================================
# API REQUEST WITH RETRIES
# ============================================================

def generate_response(prompt, max_attempts=4):
    """
    Generate a response with retries for temporary API failures.
    """

    for attempt in range(1, max_attempts + 1):

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            answer = response.text

            if not answer or not answer.strip():
                raise ValueError("The API returned an empty response.")

            return answer.strip()

        except Exception as error:

            error_message = str(error)
            error_lower = error_message.lower()

            temporary_error = any(
                marker in error_lower
                for marker in [
                    "503",
                    "unavailable",
                    "429",
                    "resource_exhausted",
                    "rate limit",
                    "500",
                    "internal server error",
                    "502",
                    "504",
                    "deadline exceeded",
                    "timed out",
                    "timeout"
                ]
            )

            if temporary_error and attempt < max_attempts:
                wait_seconds = 2 ** attempt

                print(
                    f"\nTemporary API error. "
                    f"Attempt {attempt}/{max_attempts} failed."
                )
                print(f"Retrying in {wait_seconds} seconds...")

                time.sleep(wait_seconds)

            else:
                print(f"\nRequest failed: {error_message}")

                if attempt < max_attempts:
                    print("Trying the request again...")
                    time.sleep(2 ** attempt)
                else:
                    return (
                        "EXPERIMENT FAILED\n"
                        f"Error: {error_message}\n"
                        "No successful response was generated."
                    )

    return "EXPERIMENT FAILED: Maximum retry attempts reached."


# ============================================================
# RUN ALL EXPERIMENTS
# ============================================================

def run_experiments():

    results = {}

    print("=" * 65)
    print("AI SMART AGRICULTURE & FINANCE ASSISTANT")
    print("PROMPT ENGINEERING EXPERIMENTS")
    print("=" * 65)

    print(f"\nModel: {MODEL_NAME}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("\nTest Question:")
    print(QUESTION)

    for experiment_name, prompt in PROMPTS.items():

        print("\n" + "=" * 65)
        print(experiment_name)
        print("=" * 65)

        print("\nSending prompt to Gemini API...")

        answer = generate_response(prompt)

        results[experiment_name] = {
            "prompt": prompt,
            "answer": answer
        }

        print("\nMODEL OUTPUT:\n")
        print(answer)

        # Save after every experiment so completed results
        # remain available even if a later experiment fails.
        save_results(results)

    successful = sum(
        1
        for result in results.values()
        if not result["answer"].startswith("EXPERIMENT FAILED")
    )

    print("\n" + "=" * 65)
    print("EXPERIMENT SUMMARY")
    print("=" * 65)

    print(f"Experiments completed successfully: {successful}/3")
    print("Results file: prompt_outputs.txt")

    if successful == 3:
        print("\nAll three experiments completed successfully.")
        print("You can now use the outputs to update prompt_results.md.")
    else:
        print(
            "\nSome experiments failed. Check prompt_outputs.txt "
            "for the error details."
        )


# ============================================================
# SAVE ACTUAL RESULTS
# ============================================================

def save_results(results):

    output_file = "prompt_outputs.txt"

    with open(output_file, "w", encoding="utf-8") as file:

        file.write("# Prompt Engineering Experiment Outputs\n\n")

        file.write(
            "Project: AI Smart Agriculture & Finance Assistant\n\n"
        )

        file.write(f"Model: {MODEL_NAME}\n\n")

        file.write(
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        file.write("## Experiment Question\n\n")
        file.write(QUESTION + "\n\n")

        file.write("---\n\n")

        for experiment_name, result in results.items():

            file.write(f"## {experiment_name}\n\n")

            file.write("### Prompt Used\n\n")
            file.write(result["prompt"] + "\n\n")

            file.write("### Actual Model Output\n\n")
            file.write(result["answer"] + "\n\n")

            file.write("---\n\n")


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    try:
        run_experiments()

    except KeyboardInterrupt:
        print("\nExperiment interrupted by the user.")

    except Exception as error:
        print(f"\nProgram error: {error}")