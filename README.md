# 🤖 AI Resume Analyzer

<p align="center">
  <strong>AI-powered resume analysis and job matching built with Python, Streamlit, and Google Gemini.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-red" alt="Streamlit">
  <img src="https://img.shields.io/badge/AI-Gemini-orange" alt="Gemini">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

## 📌 Overview

AI Resume Analyzer helps job seekers understand how closely their resume matches a job description. Upload a PDF resume, paste a job description, and receive an AI-generated report with scores, skills, missing keywords, improvement suggestions, learning recommendations, and interview questions.

## ✨ Features

| Feature | Description |
|---|---|
| 📄 PDF Extraction | Reads text from uploaded resumes |
| 🎯 Job Match | Estimates alignment between resume and job description |
| 📊 Resume Score | Reviews clarity, relevance, impact, and completeness |
| 🤖 ATS Score | Checks ATS-oriented structure and keyword alignment |
| ✅ Matching Skills | Identifies relevant skills already present |
| ❌ Missing Skills | Highlights skills mentioned in the job description but absent from the resume |
| 🔑 Keywords | Suggests relevant terms to consider |
| 💡 Improvements | Provides practical resume improvement ideas |
| 📚 Learning | Suggests topics that may help close skill gaps |
| 🎤 Interview Prep | Generates role-relevant interview questions |
| ⬇️ Export | Downloads the analysis as JSON |

## 🖥️ Application Flow

```text
Upload Resume (PDF)
        ↓
Paste Job Description
        ↓
     AI Analysis
        ↓
┌─────────────────────────────┐
│ Match Score                 │
│ Resume Score                │
│ ATS Score                   │
│ Matching / Missing Skills   │
│ Keywords & Improvements     │
│ Learning & Interview Prep   │
└─────────────────────────────┘
```

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **PyPDF**
- **python-dotenv**

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .env.example
├── .gitignore
│
├── utils/
│   ├── pdf_reader.py
│   └── ai_analyzer.py
│
└── screenshots/
    └── demo.png
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini

Create a `.env` file:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Do **not** commit `.env` to GitHub.

### 5. Run

```bash
streamlit run app.py
```

## 🔐 Security

API keys are loaded from environment variables and `.env` is excluded through `.gitignore`.

**Never put a real API key directly inside `app.py` or any public GitHub file.**

## ☁️ Deployment

This project can be deployed to Streamlit Community Cloud.

After pushing the repository to GitHub:

1. Open Streamlit Community Cloud.
2. Connect your GitHub repository.
3. Select `app.py`.
4. Add `GEMINI_API_KEY` under the deployment secrets.
5. Deploy.

## 📸 Screenshots

Add screenshots of your running application to:

```text
screenshots/demo.png
```

Then replace this section with:

```markdown
![AI Resume Analyzer Demo](screenshots/demo.png)
```

## 🔮 Future Improvements

- [ ] DOCX resume support
- [ ] Resume rewriting with AI
- [ ] Downloadable PDF reports
- [ ] Skill-gap charts
- [ ] Resume history
- [ ] User authentication
- [ ] Multiple job-description comparison
- [ ] Interview answer evaluation
- [ ] Streamlit deployment

## 🎓 Portfolio Description

> Developed an AI-powered Resume Analyzer using Python, Streamlit, and Google Gemini that extracts resume content from PDFs and evaluates it against job descriptions, providing ATS-oriented scoring, skill-gap analysis, keyword recommendations, resume improvement suggestions, and interview preparation.

## 📄 License

This project is licensed under the MIT License.
