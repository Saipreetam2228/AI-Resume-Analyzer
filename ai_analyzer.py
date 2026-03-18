# ai_analyzer.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# SSL (keep if needed)
os.environ['REQUESTS_CA_BUNDLE'] = 'SecurityAppliance_SSL_CA.pem'


def analyze_resume(text):
    try:
        print("Calling OpenAI API for resume analysis...")

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # faster & cheaper model
            messages=[
                {"role": "system", "content": "You are a professional resume reviewer."},
                {"role": "user", "content": f"""
Analyze this resume and provide:

1. Skills detected
2. Missing skills
3. Suggestions for improvement

Resume:
{text}
"""}
            ],
            max_tokens=500,
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI API call failed:", e)

        # 🔥 Fallback Response (VERY IMPORTANT)
        return f"""
⚠️ Live AI analysis unavailable (network issue)

--- Demo Resume Analysis ---

Skills detected:
- Python
- Machine Learning
- Data Analysis

Missing skills:
- SQL
- Deep Learning
- Communication skills

Suggestions:
- Add more project-based experience
- Include measurable achievements (e.g., improved accuracy by 20%)
- Use strong action verbs (developed, implemented, optimized)
- Improve formatting and section clarity
"""


# Test block
if __name__ == "__main__":
    sample_text = "Python developer with ML experience"
    print(analyze_resume(sample_text))

def calculate_score(text, job_role):
    text = text.lower()

    # 🔹 Predefined skills for roles
    job_skills = {
        "data scientist": ["python", "machine learning", "pandas", "numpy", "sql", "deep learning"],
        "web developer": ["html", "css", "javascript", "react", "node", "mongodb"],
        "software engineer": ["python", "java", "c++", "data structures", "algorithms"],
    }

    role = job_role.lower()

    if role not in job_skills:
        return 0, [], []

    required_skills = job_skills[role]

    matched = []
    missing = []

    for skill in required_skills:
        if skill in text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100)

    return score, matched, missing