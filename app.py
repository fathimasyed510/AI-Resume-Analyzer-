import os
import json
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

load_dotenv()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")
st.write("Analyze your resume against a job description using AI.")

def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def analyze_resume(api_key, resume_text, job_description):

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert resume and ATS analyzer.

Compare the resume with the job description.

Return ONLY valid JSON:

{{
    "match_score": 0,
    "resume_score": 0,
    "ats_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "recommended_keywords": [],
    "improvement_suggestions": [],
    "learning_suggestions": [],
    "interview_questions": []
}}

Scores must be integers from 0 to 100.

Do not invent experience or qualifications.

RESUME:
{resume_text[:30000]}

JOB DESCRIPTION:
{job_description[:20000]}
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)


# Get API key
api_key = ""

try:
    api_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    pass

if not api_key:
    api_key = os.getenv("GEMINI_API_KEY", "")

with st.sidebar:
    st.header("⚙️ Settings")

    if not api_key:
        api_key = st.text_input(
            "Gemini API Key",
            type="password"
        )

resume = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Paste Job Description",
    height=250
)

if st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
):

    if not api_key:
        st.error("Gemini API key is missing.")
        st.stop()

    if resume is None:
        st.error("Please upload your resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a job description.")
        st.stop()

    try:

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_pdf_text(resume)

            if len(resume_text.strip()) < 50:
                st.error(
                    "Could not extract enough text from the PDF."
                )
                st.stop()

            result = analyze_resume(
                api_key,
                resume_text,
                job_description
            )

        st.success("Analysis completed! 🎉")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Job Match",
            f"{result.get('match_score', 0)}%"
        )

        col2.metric(
            "Resume Score",
            f"{result.get('resume_score', 0)}/100"
        )

        col3.metric(
            "ATS Score",
            f"{result.get('ats_score', 0)}/100"
        )

        st.subheader("✅ Matching Skills")

        for skill in result.get("matching_skills", []):
            st.write("•", skill)

        st.subheader("❌ Missing Skills")

        for skill in result.get("missing_skills", []):
            st.write("•", skill)

        st.subheader("🔑 Recommended Keywords")

        for keyword in result.get("recommended_keywords", []):
            st.write("•", keyword)

        st.subheader("💡 Improvement Suggestions")

        for suggestion in result.get(
            "improvement_suggestions", []
        ):
            st.write("•", suggestion)

        st.subheader("📚 Learning Suggestions")

        for suggestion in result.get(
            "learning_suggestions", []
        ):
            st.write("•", suggestion)

        st.subheader("🎤 Interview Questions")

        for i, question in enumerate(
            result.get("interview_questions", []),
            1
        ):
            st.write(f"{i}. {question}")

        st.download_button(
            "⬇️ Download JSON Report",
            data=json.dumps(
                result,
                indent=2
            ),
            file_name="resume_analysis.json",
            mime="application/json"
        )

    except Exception as e:

        st.error("Something went wrong.")

        st.exception(e)
