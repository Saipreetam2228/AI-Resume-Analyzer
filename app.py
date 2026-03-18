from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume, calculate_score
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ SSL सेटिंग (keep as it is)
os.environ["SSL_CERT_FILE"] = r"C:\Users\III BSc\Desktop\Mini-Project_2k25\AI-Resume-Analyzer\SecurityAppliance_SSL_CA.pem"
os.environ["REQUESTS_CA_BUNDLE"] = os.environ["SSL_CERT_FILE"]
os.environ["CURL_CA_BUNDLE"] = os.environ["SSL_CERT_FILE"]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    loading = False

    # 🔥 NEW VARIABLES
    score = None
    matched = []
    missing = []

    if request.method == "POST":
        print("Form submitted")

        file = request.files.get("resume")
        job_role = request.form.get("job_role")  # ✅ NEW

        if file:
            print("File received")
            loading = True

            text = extract_text_from_pdf(file)
            print("Text extracted")

            # ✅ Step 1: AI Analysis
            result = analyze_resume(text)

            # ✅ Step 2: Score + Matching
            if job_role:
                score, matched, missing = calculate_score(text, job_role)

            loading = False

    return render_template(
        "index.html",
        result=result,
        loading=loading,
        score=score,
        matched=matched,
        missing=missing
    )

if __name__ == "__main__":
    app.run(debug=True)