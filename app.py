import os
import json
import streamlit as st
from dotenv import load_dotenv
from utils.pdf_reader import extract_text_from_pdf
from utils.ai_analyzer import analyze_resume

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖", layout="wide")

st.title("🤖 AI Resume Analyzer")
st.caption("Upload your resume and compare it with a job description using AI.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input(
        "Gemini API Key",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password",
        help="You can also store it in a .env file."
    )
    st.info("Your API key should never be committed to GitHub.")

resume_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area(
    "💼 Paste the job description",
    height=250,
    placeholder="Paste the complete job description here..."
)

if st.button("🚀 Analyze Resume", type="primary", use_container_width=True):
    if not api_key:
        st.error("Please enter your Gemini API key.")
        st.stop()
    if not resume_file:
        st.error("Please upload a PDF resume.")
        st.stop()
    if not job_description.strip():
        st.error("Please paste a job description.")
        st.stop()

    with st.spinner("Analyzing your resume..."):
        try:
            resume_text = extract_text_from_pdf(resume_file)
            if len(resume_text.strip()) < 50:
                st.error("Could not extract enough text from the PDF.")
                st.stop()

            result = analyze_resume(api_key, resume_text, job_description)
            st.session_state["result"] = result
        except Exception as e:
            st.error(f"Analysis failed: {e}")

result = st.session_state.get("result")
if result:
    st.divider()
    st.subheader("📊 Analysis Results")

    c1, c2, c3 = st.columns(3)
    c1.metric("Match Score", f"{result.get('match_score', 0)}%")
    c2.metric("Resume Score", f"{result.get('resume_score', 0)}/100")
    c3.metric("ATS Score", f"{result.get('ats_score', 0)}/100")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ Matching Skills")
        for item in result.get("matching_skills", []):
            st.write(f"• {item}")

        st.subheader("📚 Suggested Learning")
        for item in result.get("learning_suggestions", []):
            st.write(f"• {item}")

    with col2:
        st.subheader("❌ Missing Skills")
        for item in result.get("missing_skills", []):
            st.write(f"• {item}")

        st.subheader("🔑 Recommended Keywords")
        for item in result.get("recommended_keywords", []):
            st.write(f"• {item}")

    st.subheader("💡 Improvement Suggestions")
    for item in result.get("improvement_suggestions", []):
        st.write(f"• {item}")

    st.subheader("🎤 Interview Questions")
    for i, item in enumerate(result.get("interview_questions", []), 1):
        st.write(f"{i}. {item}")

    st.download_button(
        "⬇️ Download JSON Report",
        data=json.dumps(result, indent=2),
        file_name="resume_analysis.json",
        mime="application/json",
    )
