# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built with Python and Streamlit. Upload a PDF resume, paste a job description, and get an AI-generated analysis.

## ✨ Features

- 📄 PDF resume extraction
- 🎯 Job-match score
- 📊 Resume quality score
- 🤖 ATS compatibility score
- ✅ Matching skills
- ❌ Missing skills
- 🔑 Recommended keywords
- 💡 Resume improvement suggestions
- 📚 Learning suggestions
- 🎤 Interview questions
- ⬇️ Downloadable JSON report

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-dotenv

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Then add your Gemini API key:

```text
GEMINI_API_KEY=your_key_here
```

Never upload `.env` to GitHub.

### 5. Start the application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── utils/
    ├── pdf_reader.py
    └── ai_analyzer.py
```

## 🔐 Security

The `.gitignore` file excludes `.env`. Do not hard-code API keys in Python files or commit secrets to GitHub.

## 📌 Future Improvements

- DOCX resume support
- Resume rewriting
- PDF report generation
- Job-board integration
- User authentication
- Resume history
- Skill-gap charts

## 📄 License

MIT License
