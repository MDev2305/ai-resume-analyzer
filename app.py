from flask import Flask, render_template, request
import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

# Load spaCy model (lightweight)
nlp = spacy.load("en_core_web_sm")


# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text.lower()


# 🧠 Extract keywords (works for all domains)
def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text.lower())

    return list(set(keywords))


# 🤖 Lightweight similarity (no heavy models)
def get_similarity(resume, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, job_desc])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    missing_skills = []
    suggestions = []

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"].lower()

        resume_text = extract_text_from_pdf(file)

        # ✅ Use lightweight similarity
        score = get_similarity(resume_text, job_desc)

        # 🔍 Keyword comparison
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_desc)

        missing_skills = list(set(job_keywords) - set(resume_keywords))

        # 💡 Suggestions
        if missing_skills:
            suggestions.append(
                "You may consider adding: " + ", ".join(missing_skills[:10])
            )
        else:
            suggestions.append("Excellent match! Your resume aligns well.")

    return render_template(
        "index.html",
        score=score,
        missing_skills=missing_skills,
        suggestions=suggestions
    )


# 🚀 Required for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)