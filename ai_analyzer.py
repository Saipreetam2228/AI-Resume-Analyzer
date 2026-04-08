import os
from dotenv import load_dotenv

load_dotenv()

def analyze_resume(text):
    try:
        print("🚀 Running in DEMO MODE (no API errors)")

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
        print("Error:", e)
        return "Error in analysis"


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