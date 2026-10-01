import json
from google import genai

def analyze_resume(api_key, resume_text, job_description):
    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert ATS resume analyzer and career assistant.

Analyze the resume against the job description below.

Return ONLY valid JSON with exactly these keys:
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

Rules:
- Scores must be integers.
- match_score is 0-100 and represents alignment with the job.
- resume_score is 0-100 based on clarity, relevance, impact, and completeness.
- ats_score is 0-100 based on ATS-friendly structure and keywords.
- Keep lists concise and useful.
- Do not invent experience or qualifications.

RESUME:
{resume_text[:30000]}

JOB DESCRIPTION:
{job_description[:20000]}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )

    text = response.text.strip()
    return json.loads(text)
