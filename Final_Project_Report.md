# AI SMART AGRICULTURE & FINANCE ASSISTANT

### A Project Report on Prompt Engineering

**Submitted by:**
T. Sai Nikhil

**Department:** Computer Science and Engineering (Artificial Intelligence and Machine Learning)

**College:** Nadimpalli Satyanarayana Raju Institute of Technology, Visakhapatnam

**Academic Year:** 2026–2027

---

# ABSTRACT

Artificial Intelligence is increasingly used to provide information and assist users in solving everyday problems. However, the usefulness of an AI-generated response depends partly on how instructions and questions are presented to the AI model.

This project, titled **AI Smart Agriculture & Finance Assistant**, is a Python-based application developed using Streamlit and the Google Gemini API. It is designed to provide general agricultural guidance and basic financial-planning information through a simple user interface.

The project also investigates three prompt engineering techniques: Zero-Shot Prompting, Role-Based Prompting, and Structured Prompting. These techniques were tested using the same agricultural question about yellow leaves and slow growth in tomato plants. The generated responses were collected and compared to observe differences in presentation, organization, and practical guidance.

The experiment demonstrated that different prompt designs can produce responses with different structures and levels of guidance. Structured prompting was particularly useful for organizing information into predefined sections.

**Keywords:** Artificial Intelligence, Prompt Engineering, Generative AI, Gemini API, Python, Streamlit, Agriculture, Financial Planning.

---

# 1. INTRODUCTION

Artificial Intelligence has become an important technology for generating information, answering questions, and supporting decision-making.

Generative AI models can respond to user questions in natural language. However, the quality and usefulness of their responses can depend on the instructions given to them. Prompt engineering is the process of designing and refining prompts to guide an AI model toward a desired response.

The AI Smart Agriculture & Finance Assistant applies this concept by providing an interface through which users can request general agricultural guidance and financial-planning information.

In addition to developing the application, this project compares different prompting techniques to understand how prompt design influences the way an AI model presents its answers.

# 2. PROBLEM STATEMENT

Users often need understandable and practical information about agricultural problems and basic financial planning.

Although generative AI can provide such information, responses may vary in clarity, organization, and usefulness depending on how questions are framed.

Therefore, this project aims to develop an AI-based assistant and investigate how different prompt engineering techniques influence the presentation of AI-generated responses.

# 3. OBJECTIVES

The main objectives of the project are:

1. To develop an AI assistant using Python and Streamlit.
2. To integrate the Google Gemini API for generating responses.
3. To provide separate modules for agriculture and financial planning.
4. To implement Zero-Shot, Role-Based, and Structured Prompting techniques.
5. To compare responses generated using the three techniques.
6. To document the experiment results and identify the limitations of the system.

# 4. SCOPE OF THE PROJECT

The project focuses on developing a simple AI assistant and demonstrating the practical use of prompt engineering.

The application is designed to provide:

* General agricultural information and guidance.
* Basic financial-planning information.
* AI-generated responses to user questions.
* A simple interface for interacting with the assistant.

The experimental component focuses on comparing three prompting techniques using an agricultural question.

The application provides general guidance and does not replace professional agricultural, financial, or other expert advice.

# 5. TECHNOLOGIES USED

## 5.1 Python

Python is the primary programming language used to implement the application and the prompt engineering experiments.

## 5.2 Streamlit

Streamlit is used to develop the application's user interface and allow users to interact with the AI assistant.

## 5.3 Google Gemini API

The Gemini API connects the Python application to Google's generative AI model, which generates responses to user questions.

## 5.4 Prompt Engineering

Prompt engineering is used to design different instructions and compare the resulting AI responses.

## 5.5 Visual Studio Code

Visual Studio Code is used to write, organize, and execute the project code.

## 5.6 Python Libraries

The project uses libraries including:

* `streamlit` for the user interface.
* `google-genai` for communication with the Gemini API.
* `python-dotenv` for loading configuration values from an environment file.

# 6. SYSTEM DESIGN

## 6.1 System Architecture

The application's general workflow is:

**User → Streamlit Interface → Prompt Construction → Gemini API → AI-Generated Response → User**

The user enters a question through the interface. The application prepares the relevant instructions and sends the request to the Gemini API. The model generates a response, which is then displayed in the application.

For the prompt engineering experiment, a separate Python script sends the same agricultural question using three different prompting techniques. The generated responses are saved and compared.

## 6.2 Main Components

### A. User Interface

Provides an interface through which users can select a module and enter their questions.

### B. Prompt Construction

Prepares the instructions sent to the AI model. Different prompt designs can be used to guide how the model responds.

### C. Gemini API Integration

Sends prompts to the configured Gemini model and receives generated responses.

### D. Response Display

Displays the generated guidance to the user.

### E. Experiment and Evaluation

Executes the three prompting techniques, saves their outputs, and documents the observed differences.

# 7. METHODOLOGY

The project was developed in stages.

### Stage 1: Application Development

A Streamlit application was created to provide an interface for agricultural guidance and financial planning.

### Stage 2: AI Integration

The Gemini API was integrated to generate responses to user questions.

### Stage 3: Prompt Design

Three prompting techniques were selected for comparison:

1. Zero-Shot Prompting.
2. Role-Based Prompting.
3. Structured Prompting.

### Stage 4: Experiment Execution

The same agricultural question was submitted to the model using each technique.

### Stage 5: Output Collection

The Python experiment script collected the generated responses and saved them in `prompt_outputs.txt`.

### Stage 6: Comparative Evaluation

The responses were reviewed to identify differences in relevance, clarity, organization, practical recommendations, and precautions.

### Stage 7: Documentation

The experimental procedure, observations, limitations, and conclusions were documented in `prompt_results.md`.

# 8. PROMPT ENGINEERING TECHNIQUES

## 8.1 Zero-Shot Prompting

Zero-shot prompting provides the AI model with a question without additional examples or a specifically assigned role.

**Example:**

"My tomato plants have yellow leaves and slow growth. What could be the reasons, and what should I do first?"

**Purpose:** To establish a baseline response using a direct question.

## 8.2 Role-Based Prompting

Role-based prompting assigns a particular role to the AI model to encourage responses appropriate to a specific domain.

**Example:**

"Act as an agricultural extension assistant who provides practical guidance to farmers. Explain possible reasons for yellow leaves and slow growth in tomato plants and suggest practical first steps."

**Purpose:** To encourage domain-oriented explanations and practical recommendations.

## 8.3 Structured Prompting

Structured prompting combines explicit instructions with a predefined response format.

**Example structure:**

* Possible Causes
* First Steps
* Precautions
* Follow-up Questions

**Purpose:** To guide the model toward a predictable and organized response.

# 9. IMPLEMENTATION

The project contains separate files for the main application, prompt experiments, saved outputs, and experiment documentation.

## 9.1 Main Application

**File:** `app.py`

The main application uses Streamlit to provide the user interface and connects to the Gemini API to generate responses.

The application is designed to provide agricultural guidance and basic financial-planning information.

## 9.2 Experiment Script

**File:** `test_prompts.py`

This script executes the three prompt engineering experiments using the same agricultural question.

It includes retry handling for API request failures and saves experiment outputs as the experiments complete.

## 9.3 Experiment Output File

**File:** `prompt_outputs.txt`

This file stores the prompts used in the experiments and the generated responses.

It provides a record of the actual outputs used for the comparison.

## 9.4 Experiment Results File

**File:** `prompt_results.md`

This file documents the experiment objective, techniques, results, comparison, observations, conclusion, and limitations.

# 10. EXPERIMENTAL RESULTS AND COMPARISON

## 10.1 Test Question

The following question was used for all three experiments:

"My tomato plants have yellow leaves and slow growth. What could be the reasons, and what should I do first?"

## 10.2 Results

### Zero-Shot Prompting

The model identified several possible causes, including overwatering, poor drainage, nitrogen deficiency, cold temperatures, insufficient sunlight, root-bound plants, and soil pH imbalance.

It recommended checking soil moisture, observing the pattern of yellowing, and considering the plant's growing conditions.

### Role-Based Prompting

The model provided conversational, farmer-oriented guidance. It discussed watering problems, nutrient deficiencies, pests, and soil diseases.

It recommended checking soil moisture, examining the leaves, inspecting for pests, and choosing actions based on the observations.

### Structured Prompting

The model organized the response into four sections: Possible Causes, First Steps, Precautions, and Follow-up Questions.

It discussed watering imbalances, nutrient deficiencies, environmental conditions, and pests. It also included precautions against excessive fertilizer use and unnecessary chemical treatments.

## 10.3 Comparative Table

| Criterion           | Zero-Shot                  | Role-Based                      | Structured                             |
| ------------------- | -------------------------- | ------------------------------- | -------------------------------------- |
| Prompt design       | Direct question            | Assigned role                   | Role, instructions, and output format  |
| Response style      | Detailed explanation       | Conversational guidance         | Organized sections                     |
| Practical guidance  | Multiple diagnostic checks | Farmer-oriented recommendations | Categorized checks and recommendations |
| Precautions         | Included some cautions     | Included practical cautions     | Dedicated precautions section          |
| Follow-up questions | No dedicated section       | Invited further details         | Included specific questions            |

## 10.4 Key Observations

1. All three techniques produced responses relevant to the agricultural question.
2. The responses shared several possible causes and initial checks.
3. Role-based prompting encouraged a more conversational and domain-oriented style.
4. Structured prompting followed the requested headings and separated causes, actions, precautions, and follow-up questions.
5. The main differences were in the presentation and organization of the guidance rather than entirely different answers.

## 10.5 Conclusion of the Experiment

The experiment demonstrated that different prompting techniques can influence how AI-generated information is presented.

For the tested question, structured prompting was particularly useful for producing a predictable response format. However, this experiment does not establish that structured prompting is always more accurate or effective.

The findings are limited to the tested question and should be evaluated further using additional questions and domains.

# 11. LIMITATIONS

The project has the following limitations:

1. The prompt comparison experiment focuses on one primary agricultural question.
2. AI-generated responses can vary across repeated runs.
3. The system depends on the availability and configuration of the Gemini API.
4. The experimental evaluation is qualitative rather than based on a standardized scoring system.
5. The agricultural recommendations have not all been independently verified.
6. Financial-planning responses provide general information rather than personalized professional advice.

# 12. FUTURE ENHANCEMENTS

Possible future improvements include:

1. Testing additional prompting techniques and more questions.
2. Evaluating responses using a consistent scoring rubric.
3. Expanding agricultural guidance to different crops and plant problems.
4. Improving financial-planning guidance with appropriate safeguards.
5. Adding multilingual support for users who prefer regional languages.
6. Improving error reporting and handling for API failures.
7. Conducting more systematic evaluations of the relevance and reliability of generated responses.

# 13. CONCLUSION

The AI Smart Agriculture & Finance Assistant demonstrates the integration of generative AI into a simple application for agricultural guidance and basic financial planning.

The project also provides a practical demonstration of prompt engineering by comparing Zero-Shot Prompting, Role-Based Prompting, and Structured Prompting.

The experiments showed that different prompt designs can produce responses with different styles and levels of organization. Structured prompting was particularly useful for arranging information into predefined sections.

The project helped demonstrate the practical use of Python, Streamlit, API integration, and prompt engineering in an AI-based application.

Further testing and evaluation would be necessary to establish the accuracy, reliability, and broader effectiveness of the system.

# 14. REFERENCES

1. Google AI for Developers, Gemini API Documentation: https://ai.google.dev/gemini-api/docs
2. Streamlit Documentation: https://docs.streamlit.io/
3. Python Documentation: https://docs.python.org/3/
4. Google Gen AI Python SDK: https://github.com/googleapis/python-genai

---

**Project Title:** AI Smart Agriculture & Finance Assistant

**Project Focus:** Generative AI and Prompt Engineering

**End of Report**
