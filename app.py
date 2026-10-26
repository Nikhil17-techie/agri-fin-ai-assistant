import os
import time
import streamlit as st
from dotenv import load_dotenv
from google import genai


# ============================================================
# 1. CONFIGURATION
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="AgriFin AI | Smart Agriculture & Finance",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

client = genai.Client(api_key=API_KEY) if API_KEY else None


# ============================================================
# 2. APPLICATION THEME
# ============================================================

st.markdown(
    """
    <style>
    /* ========================================================
       COLOR PALETTE
       Background: soft green-white
       Headings: forest green
       Body text: charcoal
       Cards: white
       Buttons: natural green
       ======================================================== */

    :root {
        --page-bg: #F2F7F0;
        --surface: #FFFFFF;
        --heading: #174C35;
        --body-text: #26352C;
        --muted-text: #5C6F61;
        --primary: #26734D;
        --primary-hover: #1B593A;
        --border: #D8E5D9;
        --soft-green: #E6F1E7;
    }

    /* Main application background */
    .stApp {
        background: var(--page-bg);
        color: var(--body-text);
    }

    /* Main content area */
    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ========================================================
       FIX ALL MAIN HEADINGS
       Prevent headings from becoming white.
       ======================================================== */

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6 {
        color: var(--heading) !important;
        font-weight: 700 !important;
    }

    /* Main page title */
    .stApp h1 {
        letter-spacing: -0.5px;
    }

    /* Markdown body text */
    .stApp p,
    .stApp li,
    .stApp label,
    .stApp .stMarkdown,
    .stApp .stMarkdown p,
    .stApp .stMarkdown li {
        color: var(--body-text);
    }

    /* Strong/bold text */
    .stApp strong,
    .stApp b {
        color: var(--heading) !important;
    }

    /* Caption text */
    .stApp .stCaption,
    .stApp [data-testid="stCaptionContainer"] {
        color: var(--muted-text) !important;
    }

    /* ========================================================
       SIDEBAR
       White text is intentional ONLY in the dark sidebar.
       ======================================================== */

    section[data-testid="stSidebar"] {
        background: #173F2D !important;
        border-right: 1px solid #244D39;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div {
        color: #FFFFFF;
    }

    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #E0ECE3;
    }

    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        background: var(--primary) !important;
        color: #FFFFFF !important;
        border: 1px solid var(--primary) !important;
        border-radius: 10px !important;
        min-height: 44px;
        font-weight: 600 !important;
        transition: background 0.2s ease, transform 0.2s ease;
    }

    .stButton > button p,
    .stButton > button span {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background: var(--primary-hover) !important;
        border-color: var(--primary-hover) !important;
        transform: translateY(-1px);
    }

    /* Download button */
    .stDownloadButton > button {
        background: #FFFFFF !important;
        color: var(--heading) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }

    .stDownloadButton > button p,
    .stDownloadButton > button span {
        color: var(--heading) !important;
    }

    .stDownloadButton > button:hover {
        background: var(--soft-green) !important;
        border-color: var(--primary) !important;
    }

    /* ========================================================
       INPUT FIELDS
       ======================================================== */

    .stTextArea textarea,
    .stTextInput input {
        background: #FFFFFF !important;
        color: #171717 !important;
        border: 1px solid #CBDACD !important;
        border-radius: 10px !important;
    }

    .stTextArea textarea::placeholder,
    .stTextInput input::placeholder {
        color: #77847A !important;
        opacity: 1;
    }

    .stTextArea textarea:focus,
    .stTextInput input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 2px rgba(38, 115, 77, 0.12) !important;
    }

    /* Radio labels */
    .stRadio label,
    .stRadio label p {
        color: var(--body-text) !important;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background: #FFFFFF !important;
        border-color: #CBDACD !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] * {
        color: #26352C !important;
    }

    /* ========================================================
       INFORMATION CARDS
       ======================================================== */

    .info-card {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 24px;
        min-height: 155px;
        margin-bottom: 16px;
        box-shadow: 0 5px 20px rgba(23, 76, 53, 0.05);
    }

    .info-card h3 {
        color: var(--heading) !important;
        margin-top: 0;
        margin-bottom: 12px;
        font-size: 1.2rem;
    }

    .info-card p {
        color: var(--body-text) !important;
        line-height: 1.7;
        margin-bottom: 0;
    }

    /* ========================================================
       ANSWER CARD
       Both Simple and Detailed answers use this same design.
       ======================================================== */

    .st-key-answer_container {
        background: #FFFFFF !important;
        border: 1px solid var(--border) !important;
        border-left: 5px solid var(--primary) !important;
        border-radius: 14px !important;
        padding: 20px !important;
        box-shadow: 0 5px 20px rgba(23, 76, 53, 0.05);
    }

    /* Force every answer heading to dark forest green */
    .st-key-answer_container h1,
    .st-key-answer_container h2,
    .st-key-answer_container h3,
    .st-key-answer_container h4,
    .st-key-answer_container h5,
    .st-key-answer_container h6 {
        color: #174C35 !important;
        font-weight: 700 !important;
    }

    /* Force answer body text to black */
    .st-key-answer_container p,
    .st-key-answer_container li,
    .st-key-answer_container span,
    .st-key-answer_container div,
    .st-key-answer_container em,
    .st-key-answer_container strong,
    .st-key-answer_container b {
        color: #000000 !important;
    }

    /* Answer lists */
    .st-key-answer_container ul,
    .st-key-answer_container ol {
        padding-left: 25px;
    }

    .st-key-answer_container li {
        margin-bottom: 7px;
        line-height: 1.65;
    }

    .st-key-answer_container p {
        line-height: 1.75;
    }

    /* Answer code blocks */
    .st-key-answer_container pre {
        background: #F3F5F3 !important;
        border: 1px solid #DCE5DC;
        border-radius: 8px;
        padding: 12px;
    }

    .st-key-answer_container code {
        color: #172B1E !important;
    }

    /* ========================================================
       EXPANDERS
       ======================================================== */

    .stApp [data-testid="stExpander"] {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 12px;
    }

    .stApp [data-testid="stExpander"] summary {
        color: var(--heading) !important;
    }

    /* ========================================================
       ALERTS
       ======================================================== */

    .stAlert p {
        color: #26352C !important;
    }

    /* Divider */
    hr {
        border-color: var(--border) !important;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: var(--muted-text);
        font-size: 13px;
        line-height: 1.8;
        padding: 20px 0;
    }

    /* Responsive layout */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 1rem;
        }

        .info-card {
            padding: 18px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 3. SESSION STATE
# ============================================================

defaults = {
    "page": "Home",
    "history": [],
    "answer": "",
    "last_question": "",
    "last_module": "",
    "last_style": "Simple",
    "notice": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# 4. HELPER FUNCTIONS
# ============================================================

def navigate(page):
    st.session_state.page = page
    st.session_state.notice = ""


def clear_current_answer():
    st.session_state.answer = ""
    st.session_state.last_question = ""
    st.session_state.last_module = ""
    st.session_state.last_style = "Simple"
    st.session_state.notice = ""


def get_module_instructions(module):
    if module == "Agriculture":
        return """
You are an agricultural guidance assistant.

You can help with:
- Crop care and plant symptoms
- Soil health and irrigation
- General farming practices
- Common pest and plant health concerns

Give practical, understandable guidance.

Do not diagnose a disease with certainty based only on a
short description. Do not invent pesticide doses or chemical
application rates. Recommend a qualified local agricultural
expert when symptoms are serious or unclear.
"""

    return """
You are a basic financial planning assistant.

You can help with:
- Personal budgeting
- Saving habits
- Basic financial literacy
- General financial planning
- General information about government schemes

Do not guarantee investment returns or financial outcomes.
Do not invent scheme eligibility, deadlines, or benefits.
Encourage verification through official government sources.

Never request passwords, OTPs, PINs, or complete bank details.
"""


def build_prompt(question, module, answer_style):
    if answer_style == "Simple":
        response_style = """
ANSWER STYLE: SIMPLE

- Use plain, everyday English.
- Begin with a direct answer.
- Keep the explanation concise and useful.
- Give three to five practical steps when appropriate.
- Include important precautions.
- Use short headings and bullet points where helpful.
- Avoid unnecessary technical terms.
"""
    else:
        response_style = """
ANSWER STYLE: DETAILED

- Explain the topic thoroughly and clearly.
- Use meaningful headings and subheadings.
- Explain important causes, background, or context.
- Give step-by-step practical recommendations.
- Explain why important recommendations matter.
- Include examples where helpful.
- Include relevant risks, limitations, and precautions.
- Use numbered lists and bullet points for readability.
- Avoid unsupported claims and unnecessary repetition.
"""

    return f"""
You are AgriFin AI, an AI Smart Agriculture & Finance Assistant.

SELECTED MODULE:
{module}

MODULE INSTRUCTIONS:
{get_module_instructions(module)}

USER QUESTION:
{question}

{response_style}

QUESTION VALIDATION:
First determine whether the question belongs to the selected module.

If the question belongs to the selected module, answer it.

If the question belongs to the other module, return exactly:
STATUS: OTHER
ANSWER: Please ask a question related to {module}.

If the question is unrelated to both modules, return:
STATUS: OTHER
ANSWER: This question is outside the scope of AgriFin AI.
Please ask a question related to {module}.

If the question is too vague to understand, return:
STATUS: UNCLEAR
ANSWER: Please provide more information about your question.

For a relevant question, return:
STATUS: MATCH
ANSWER:
Write the complete answer here.

Do not put STATUS or MATCH inside the actual answer.

Use Markdown formatting for headings, lists, and important points.
Never claim that general guidance replaces professional advice.
"""


def generate_guidance(question, module, answer_style):
    if client is None:
        return (
            "ERROR",
            "API key not found. Please check GEMINI_API_KEY "
            "in your .env file."
        )

    prompt = build_prompt(question, module, answer_style)

    for attempt in range(2):
        try:
            print("DEBUG MODEL:", repr(MODEL_NAME))
            response = client.models.generate_content(
                 model="gemini-3.8-flash",
                 contents=prompt
                 )
            
            response_text = (response.text or "").strip()

            if not response_text:
                return (
                    "ERROR",
                    "The AI returned an empty response. Please try again."
                )

            status = "MATCH"
            answer = response_text

            lines = response_text.splitlines()
            status_found = False
            reading_answer = False
            answer_lines = []

            for line in lines:
                stripped = line.strip()

                if stripped.upper().startswith("STATUS:"):
                    status = stripped.split(":", 1)[1].strip().upper()
                    status_found = True
                    continue

                if stripped.upper().startswith("ANSWER:"):
                    reading_answer = True
                    first_part = stripped.split(":", 1)[1].strip()

                    if first_part:
                        answer_lines.append(first_part)

                    continue

                if reading_answer:
                    answer_lines.append(line)

            if status_found and answer_lines:
                answer = "\n".join(answer_lines).strip()

            if status not in ("MATCH", "OTHER", "UNCLEAR"):
                status = "MATCH"
                answer = response_text

            if not answer:
                answer = response_text

            return status, answer

        except Exception as error:
            error_text = str(error).lower()

            temporary_error = any(
                term in error_text
                for term in [
                    "503",
                    "429",
                    "unavailable",
                    "high demand",
                    "resource_exhausted",
                ]
            )

            if temporary_error and attempt == 0:
                time.sleep(2)
                continue

            if "404" in error_text or "not found" in error_text:
                return (
                    "ERROR",
                    f"The configured model '{MODEL_NAME}' may not be "
                    "available. Check GEMINI_MODEL in your .env file "
                    "and use a model available to your API key.",
                )

            if "api key" in error_text or "401" in error_text:
                return (
                    "ERROR",
                    "The API key may be invalid. Check your .env file "
                    "without sharing your key with anyone.",
                )

            if temporary_error:
                return (
                    "ERROR",
                    "Gemini is temporarily busy or a usage limit was "
                    "reached. Wait a little and try again.",
                )

            return (
                "ERROR",
                f"Unable to generate guidance: {error}",
            )

    return "ERROR", "Unable to generate guidance right now."


def process_question(question, module, answer_style):
    question = question.strip()

    if not question:
        st.warning("Please enter a question first.")
        return

    with st.spinner("🌱 AgriFin AI is preparing your guidance..."):
        status, answer = generate_guidance(
            question,
            module,
            answer_style,
        )

    if status == "ERROR":
        st.error(answer)
        return

    if status == "OTHER":
        st.warning(answer)
        return

    if status == "UNCLEAR":
        st.info(answer)
        return

    st.session_state.answer = answer
    st.session_state.last_question = question
    st.session_state.last_module = module
    st.session_state.last_style = answer_style
    st.session_state.notice = "Guidance generated successfully!"

    st.session_state.history.insert(
        0,
        {
            "question": question,
            "module": module,
            "style": answer_style,
            "answer": answer,
        },
    )


def show_answer():
    if not st.session_state.answer:
        return

    st.markdown("### 🌿 AI Guidance")

    # Streamlit container with a unique key.
    # CSS above applies black text to answer paragraphs and lists,
    # while keeping answer headings dark green.
    with st.container(
        border=True,
        key="answer_container",
    ):
        st.markdown(st.session_state.answer)

    st.download_button(
        label="📥 Download Guidance as TXT",
        data=(
            f"AgriFin AI - {st.session_state.last_module}\n\n"
            f"Question: {st.session_state.last_question}\n\n"
            f"Answer Style: {st.session_state.last_style}\n\n"
            f"Guidance:\n{st.session_state.answer}\n"
        ),
        file_name="agrifin_ai_guidance.txt",
        mime="text/plain",
    )


def render_module_page(module, examples):
    if module == "Agriculture":
        st.markdown("# 🌾 Agriculture Guidance")
        st.markdown(
            "Get general guidance about crops, plant symptoms, "
            "soil health, irrigation, and farming practices."
        )
        question_label = "Enter your agriculture question:"
        question_placeholder = (
            "Example: My tomato plants have yellow leaves. "
            "What should I check first?"
        )
        generate_label = "🌱 Generate Guidance"
        question_key = "agriculture_question"
        style_key = "agriculture_style"
        example_key = "agriculture_example"
        generate_key = "agriculture_generate"
        clear_key = "agriculture_clear"

    else:
        st.markdown("# 💰 Financial Planning")
        st.markdown(
            "Explore budgeting, saving, financial literacy, "
            "and general information about financial schemes."
        )
        question_label = "Enter your financial planning question:"
        question_placeholder = (
            "Example: How can a student save money every month?"
        )
        generate_label = "💰 Generate Guidance"
        question_key = "finance_question"
        style_key = "finance_style"
        example_key = "finance_example"
        generate_key = "finance_generate"
        clear_key = "finance_clear"

    st.markdown("### 💡 Suggested Questions")

    selected_example = st.selectbox(
        "Choose an example or enter your own question below:",
        ["Select an example..."] + examples,
        key=example_key,
    )

    default_question = (
        selected_example
        if selected_example != "Select an example..."
        else ""
    )

    question = st.text_area(
        question_label,
        value=default_question,
        height=130,
        placeholder=question_placeholder,
        key=question_key,
    )

    answer_style = st.radio(
        "Answer style",
        ["Simple", "Detailed"],
        horizontal=True,
        key=style_key,
        help=(
            "Simple provides a concise answer. Detailed provides "
            "more explanation and practical steps."
        ),
    )

    col1, col2 = st.columns([3, 1])

    with col1:
        generate_clicked = st.button(
            generate_label,
            key=generate_key,
            use_container_width=True,
        )

    with col2:
        clear_clicked = st.button(
            "🗑️ Clear",
            key=clear_key,
            use_container_width=True,
        )

    if clear_clicked:
        clear_current_answer()
        st.rerun()

    if generate_clicked:
        process_question(question, module, answer_style)

    if st.session_state.notice:
        if st.session_state.last_module == module:
            st.success(st.session_state.notice)
            st.session_state.notice = ""

    if st.session_state.last_module == module:
        show_answer()


# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding:18px 0 20px 0;">
            <div style="font-size:48px;">🌱</div>
            <h2 style="color:#FFFFFF !important; margin:0;">
                AgriFin AI
            </h2>
            <p style="color:#E0ECE3 !important; font-size:13px;">
                Smart Agriculture & Finance
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    if st.button("🏠 Home", use_container_width=True):
        navigate("Home")
        st.rerun()

    if st.button("🌾 Agriculture", use_container_width=True):
        navigate("Agriculture")
        st.rerun()

    if st.button("💰 Financial Planning", use_container_width=True):
        navigate("Financial Planning")
        st.rerun()

    if st.button("📚 History", use_container_width=True):
        navigate("History")
        st.rerun()

    if st.button("ℹ️ About", use_container_width=True):
        navigate("About")
        st.rerun()

    st.markdown("---")

    st.caption("AI-powered general guidance")
    st.caption(
        "Verify important agricultural and financial decisions "
        "with qualified experts or official sources."
    )


# ============================================================
# 6. HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown("# 🌱 AI Smart Agriculture & Finance Assistant")

    st.markdown(
        """
        Welcome to **AgriFin AI** — your smart assistant for
        general agricultural guidance and basic financial planning.
        """
    )

    st.markdown("## ✨ What can AgriFin AI do?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>🌾 Agriculture Guidance</h3>
                <p>
                    Explore crop care, plant symptoms, soil health,
                    irrigation, and general farming practices.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Open Agriculture Module →",
            key="home_agriculture",
            use_container_width=True,
        ):
            navigate("Agriculture")
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>💰 Financial Planning</h3>
                <p>
                    Learn about budgeting, saving, basic financial
                    planning, and government financial schemes.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Open Financial Planning →",
            key="home_finance",
            use_container_width=True,
        ):
            navigate("Financial Planning")
            st.rerun()

    st.markdown("## 🌟 Key Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown(
            """
            <div class="info-card">
                <h3>🧠 AI Guidance</h3>
                <p>
                    Receive AI-generated answers using structured
                    prompts and module-specific instructions.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with f2:
        st.markdown(
            """
            <div class="info-card">
                <h3>📝 Two Answer Styles</h3>
                <p>
                    Choose Simple or Detailed explanations to suit
                    your needs.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with f3:
        st.markdown(
            """
            <div class="info-card">
                <h3>📥 Save Your Answers</h3>
                <p>
                    Download guidance and review previous answers
                    during your current session.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(
        "Choose a module from the sidebar or use one of the "
        "buttons above to get started."
    )


# ============================================================
# 7. AGRICULTURE
# ============================================================

elif st.session_state.page == "Agriculture":

    agriculture_examples = [
        (
            "My tomato plants have yellow leaves and slow growth. "
            "What could be the reasons, and what should I do first?"
        ),
        "How can I improve soil health for vegetable crops?",
        "What are general ways to use water efficiently on a farm?",
        "What should I check if my crop is growing slowly?",
    ]

    render_module_page("Agriculture", agriculture_examples)


# ============================================================
# 8. FINANCIAL PLANNING
# ============================================================

elif st.session_state.page == "Financial Planning":

    finance_examples = [
        "How can a college student create a monthly budget?",
        "What is an emergency fund, and why is it important?",
        "How can I start saving money with a small monthly income?",
        (
            "What should I check before applying for a government "
            "financial assistance scheme?"
        ),
    ]

    render_module_page("Financial Planning", finance_examples)


# ============================================================
# 9. HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.markdown("# 📚 Question History")

    st.markdown(
        "Review the questions and answers generated during "
        "your current application session."
    )

    if not st.session_state.history:
        st.info(
            "No history yet. Generate guidance from either module "
            "to see your previous questions here."
        )

    else:
        if st.button("🗑️ Clear History", key="clear_history"):
            st.session_state.history = []
            st.rerun()

        for index, item in enumerate(st.session_state.history):

            with st.expander(
                f"{index + 1}. {item['module']} — {item['question']}"
            ):
                st.caption(f"Answer style: {item['style']}")

                with st.container(
                    border=True,
                    key=f"history_answer_{index}",
                ):
                    st.markdown(item["answer"])

                st.download_button(
                    label="📥 Download this answer",
                    data=(
                        f"AgriFin AI\n"
                        f"Module: {item['module']}\n"
                        f"Question: {item['question']}\n"
                        f"Answer Style: {item['style']}\n\n"
                        f"{item['answer']}"
                    ),
                    file_name=f"agrifin_guidance_{index + 1}.txt",
                    mime="text/plain",
                    key=f"history_download_{index}",
                )


# ============================================================
# 10. ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.markdown("# ℹ️ About AgriFin AI")

    st.markdown(
        """
        <div class="info-card">
            <h3>🌱 Project Overview</h3>
            <p>
                AI Smart Agriculture & Finance Assistant is an
                educational prompt-engineering project that provides
                general agricultural guidance and basic financial
                planning information using AI.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## 🎯 Project Objectives")

    st.markdown(
        """
        - Provide accessible AI-generated general guidance.
        - Demonstrate structured prompt engineering.
        - Compare concise and detailed response styles.
        - Separate agricultural and financial questions.
        - Let users review and download generated answers.
        """
    )

    st.markdown("## 🛠️ Technologies Used")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>Python</h3>
                <p>Core application programming language.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>Streamlit</h3>
                <p>Interactive web application framework.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="info-card">
                <h3>Google Gemini</h3>
                <p>AI-powered response generation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("## ⚠️ Responsible Use")

    st.warning(
        "AgriFin AI provides general information, not guaranteed "
        "professional advice. Verify important agricultural "
        "recommendations with qualified experts and financial "
        "scheme information through official government sources."
    )

    st.markdown("## ⚙️ Model Configuration")

    st.code(
        f"Configured Gemini model: {MODEL_NAME}",
        language="text",
    )


# ============================================================
# 11. FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer-text">
        🌱 AgriFin AI | AI Smart Agriculture & Finance Assistant
        <br>
        Built with Python, Streamlit, and Google Gemini
        <br>
        For educational and informational purposes
    </div>
    """,
    unsafe_allow_html=True,
)