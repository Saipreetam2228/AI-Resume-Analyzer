# AI Resume Analyzer

An AI-powered web application that analyzes resumes, matches them with target job roles, and provides actionable improvement suggestions.

---

## 🚀 Features

- Upload resume (PDF)
- Extract and process text
- Identify key skills
- Match skills with job role
- Generate resume score
- Highlight matched & missing skills
- Provide AI-based suggestions

---

## 🛠 Tech Stack

- Python
- Flask
- OpenAI API
- NLP (Text Processing)
- HTML / CSS

---

## 📂 Project Structure
```
ai-resume-analyzer/
├── templates/
│   └── index.html
├── ai_analyzer.py
├── app.py
├── resume_parser.py
├── requirements.txt
├── Procfile
└── runtime.txt

```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/your-username/ai-resume-analyzer.git  
cd ai-resume-analyzer  
```

### 2. (Optional but Recommended) Create Virtual Environment

Windows:
```
venv\Scripts\activate  
```
Mac/Linux:
```
source venv/bin/activate  
```

### 3. Install Dependencies
```
pip install -r requirements.txt  
```

### 4. Add Environment Variables
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_api_key_here  
```

### 5. Run the Application
```
python app.py  
```

### 6. Open in Browser
```
http://127.0.0.1:5000  
```

## 🌐 Deployment (Render)

Steps:

1. Push code to GitHub  
2. Go to Render  
3. Create New Web Service  
4. Connect your repository  
5. Add environment variable:
   OPENAI_API_KEY  
6. Deploy  

---

## 📊 How It Works

1. User uploads resume  
2. Text is extracted  
3. Skills are identified  
4. Compared with job role  
5. Score is calculated  
6. Suggestions are generated  

---

## 🎯 Future Improvements

- Job description matching  
- Resume PDF report download  
- User authentication  
- Resume history  
- Advanced ATS scoring  

---

## 📌 Author

Developed by Your Name  

---

## ⭐ Support

If you like this project, give it a star on GitHub!
