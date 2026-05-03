from flask import Flask, render_template, request
import PyPDF2
import spacy
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)


nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')



def extract_text_from_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text.lower()



def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text.lower())

    return list(set(keywords))



def semantic_score(resume, job_desc):
    emb1 = model.encode(resume, convert_to_tensor=True)
    emb2 = model.encode(job_desc, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return round(float(score) * 100, 2)


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    missing_skills = []
    suggestions = []

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"].lower()

        resume_text = extract_text_from_pdf(file)

        
        score = semantic_score(resume_text, job_desc)

       
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_desc)

        missing_skills = list(set(job_keywords) - set(resume_keywords))

       
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


if __name__ == "__main__":
    app.run(debug=True)