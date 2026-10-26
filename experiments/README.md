# AI Smart Agriculture & Financial Decision Support Assistant

AgriFin AI Assistant is an AI-powered application built with Python and Streamlit. It provides general agricultural guidance and basic financial planning support using Google's Gemini API.

## Features

* Agriculture question-and-answer support
* Basic financial planning assistance
* AI-generated responses using the Gemini API
* Interactive Streamlit interface
* Prompt engineering and response formatting
* Safety disclaimers and guidance limitations

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* python-dotenv
* Prompt Engineering

## Project Structure

* `app.py` — Main Streamlit application
* `check_gemini.py` — Gemini API testing script, if applicable
* `test_prompts.py` — Prompt testing script, if applicable
* `Final_Project_Report.md` — Project documentation and report
* `requirements.txt` — Python dependencies
* `.gitignore` — Excludes sensitive and unnecessary files

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd agri-fin-ai-assistant
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project folder and add:

`GEMINI_API_KEY=your_api_key_here`

Replace the placeholder with your own Gemini API key.

Never publish your actual API key.

### 5. Run the application

```bash
python -m streamlit run app.py
```

## Limitations

The application provides general informational guidance. Agricultural recommendations may require verification by local agricultural experts. Financial responses are educational and should not replace advice from a qualified financial professional.

## Author

Sai Nikhil
