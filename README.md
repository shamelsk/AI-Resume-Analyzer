# 🤖 ResumeIQ AI – AI Powered Resume Analyzer

> An AI-powered Resume Analyzer that evaluates resumes using Google's Gemini LLM and provides ATS-focused insights, skill gap analysis, personalized suggestions, and a downloadable PDF report.


---

## 📌 Overview

ResumeIQ AI is a Generative AI application that helps job seekers improve their resumes by leveraging Google's Gemini Large Language Model.

Users simply upload a resume in PDF format, and the application extracts the text, analyzes it using AI, and generates a detailed evaluation including resume scores, strengths, weaknesses, missing skills, improvement suggestions, and recommended job roles.

The application also generates a downloadable PDF report for future reference.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 🤖 AI-Powered Resume Analysis using Gemini
- 📊 Overall Resume Score
- 📈 ATS Compatibility Score
- 💻 Technical Skills Evaluation
- 🚀 Project Evaluation
- 🎓 Education Assessment
- 💼 Experience Assessment
- 💪 Resume Strengths
- ⚠ Resume Weaknesses
- 📚 Missing Skills Identification
- 💡 Personalized Improvement Suggestions
- 🎯 Recommended Job Roles
- 📥 Download AI Analysis Report as PDF

---

## 🧠 Key Concepts Demonstrated

- Generative AI
- Prompt Engineering
- Large Language Models (LLMs)
- Structured JSON Output
- PDF Processing
- Streamlit Development
- API Integration
- Report Generation
- Error Handling

---

## 🛠 Tech Stack

Python 
Streamlit 
Google Gemini API 
PyMuPDF 
ReportLab 
JSON 
python-dotenv 

---

## 🏗 Project Architecture

```
User Uploads Resume
        │
        ▼
PDF Text Extraction (PyMuPDF)
        │
        ▼
Prompt Engineering
        │
        ▼
Google Gemini API
        │
        ▼
Structured JSON Response
        │
        ▼
Resume Dashboard
        │
        ▼
Download PDF Report
```

---

## 📂 Project Structure

```
ResumeIQ-AI/
│
├── app.py
├── analyzer.py
├── pdf_parser.py
├── prompts.py
├── report_generator.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (Not included)
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ResumeIQ-AI.git
```

```bash
cd ResumeIQ-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Generate your API key from Google AI Studio.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 AI Analysis Output

The application generates:

- Overall Resume Score
- ATS Score
- Skills Score
- Projects Score
- Experience Score
- Education Score
- Resume Strengths
- Resume Weaknesses
- Missing Skills
- Improvement Suggestions
- Recommended Job Roles


---

## 💡 Future Improvements

- Resume vs Job Description Matching
- AI Resume Rewriter
- AI Interview Preparation Assistant
- Interactive Dashboard with Charts
- Multi-language Resume Support
- Dark Mode

---

## 👨‍💻 Author

**Sheetal Gupta**

B.Tech Computer Science Engineering

Interested in AI • Machine Learning • Generative AI • Backend Development
