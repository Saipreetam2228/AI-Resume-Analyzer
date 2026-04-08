# ai_analyzer.py

import os
from dotenv import load_dotenv

# Try Gemini (new SDK)
try:
    from google import genai
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    GEMINI_AVAILABLE = True
except:
    GEMINI_AVAILABLE = False

load_dotenv()


def analyze_resume(text):
    try:
        # ✅ If Gemini works
        if GEMINI_AVAILABLE:
            print("🚀 Using Gemini API...")

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"""
You are an expert ATS resume analyzer.

Analyze the resume and give:

1. Skills detected
2. Missing skills
3. Suggestions

Resume:
{text}
"""
            )

            return response.text

        # ✅ Fallback (DEMO MODE)
        else:
            print("🚀 Running in DEMO MODE (no API)")

            return f"""
--- Resume Analysis ---

Skills detected:
- Python
- Machine Learning
- Data Analysis

Missing skills:
- SQL
- Deep Learning
- Communication

Suggestions:
- Add more real-world projects
- Include measurable achievements
- Improve formatting

(Preview based on your resume content)
"""

    except Exception as e:
        print("❌ Error:", e)

        # ✅ Safe fallback (VERY IMPORTANT)
        return f"""
⚠️ AI temporarily unavailable

--- Resume Analysis ---

Skills detected:
- Python
- Machine Learning
- Data Analysis

Missing skills:
- SQL
- Deep Learning
- Communication

Suggestions:
- Add more projects
- Add achievements
- Improve clarity
"""


def calculate_score(text, job_role):
    text = text.lower()

    job_skills = {
        "data scientist": ["python", "machine learning", "pandas", "numpy", "sql", "deep learning"],
        "web developer": ["html", "css", "javascript", "react", "node", "mongodb"],
        "software engineer": ["python", "java", "c++", "data structures", "algorithms"],
    }

    role = job_role.lower()

    if role not in job_skills:
        return 0, [], []

    required = job_skills[role]

    matched = [s for s in required if s in text]
    missing = [s for s in required if s not in text]

    score = int((len(matched) / len(required)) * 100)

    return score, matched, missing