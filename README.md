# 📄 AI Resume Analyzer

An intelligent, AI-powered web application that evaluates resumes against job descriptions using advanced Natural Language Processing (NLP) and semantic similarity techniques.

This project is designed to simulate real-world resume screening systems by dynamically extracting relevant skills, understanding contextual meaning, and providing actionable feedback to improve candidate-job alignment.

---

## Features

* 📄 Upload resume (PDF support)
* 📝 Paste job description
* 📊 Match score using semantic similarity
* 🔍 Dynamic keyword extraction (no fixed skill list)
* ⚠️ Skill gap detection
* 💡 Smart suggestions for improvement
* 🌐 Clean and interactive UI

---

## How It Works

* Extracts text from resume (PDF parsing)
* Uses **spaCy NLP** to identify meaningful keywords
* Applies **Sentence Transformers** for semantic similarity scoring
* Compares resume and job description to detect missing skills
* Generates suggestions based on gaps

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **NLP:** spaCy
* **AI Models:** Sentence Transformers
* **Frontend:** HTML, CSS, JavaScript
* **Other Tools:** PyPDF2, Scikit-learn

---

## 📁 Project Structure

```
resume-analyzer/
│
├── app.py
├── templates/
│     └── index.html
├── static/
│     ├── style.css
│     └── script.js
├── requirements.txt
└── README.md
```

---
## Live Demo
https://ai-resume-analyzer-a6lz.onrender.com

##  Run Locally

```bash
git clone https://github.com/MDev2305/ai-resume-analyzer.git
cd ai-resume-analyzer

pip install -r requirements.txt
python app.py
```

Then open:
👉 http://127.0.0.1:5000/

---


## 🚀 Future Improvements

* 🤖 AI-generated resume feedback (LLM integration)
* 🎯 Role-based analysis (tech vs non-tech detection)
* 📊 Advanced dashboard with charts
* 🌍 Multi-language support

---


GitHub: https://github.com/MDev2305

