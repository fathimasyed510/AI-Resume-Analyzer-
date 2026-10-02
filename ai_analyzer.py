import json
from google import genai

def analyze_resume(api_key, resume_text, job_description):
    client = genai.Client(api_key=api_key)
    prompt = f'''You are an expert ATS resume analyzer and career assistant.
Analyze the resume against the job description.
Return ONLY valid JSON with exactly these keys:
{{"match_score":0,"resume_score":0,"ats_score":0,"matching_skills":[],"missing_skills":[],"recommended_keywords":[],"improvement_suggestions":[],"learning_suggestions":[],"interview_questions":[]}}
Scores must be integers. Scores are 0-100. Keep lists concise. Do not invent experience or qualifications.
RESUME:\n{resume_text[:30000]}
JOB DESCRIPTION:\n{job_description[:20000]}'''
    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt, config={'response_mime_type': 'application/json'})
    return json.loads(response.text.strip())
