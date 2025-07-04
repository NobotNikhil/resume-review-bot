
# 📄 Resume Review Bot (AI-Powered)

A simple Streamlit app to analyze resumes in PDF format using AI or fallback logic.

---

## ✨ Features

- 📤 Upload any resume (PDF only)
- 📄 Extracts text from the resume
- 🧠 AI-powered analysis using OpenRouter (Mistral 7B)
- 🧪 Fallback rule-based feedback if no API key is set
- 🔎 Feedback includes:
  - Strengths
  - Missing sections
  - Suggestions for improvement

---

## 🚀 How to Run Locally

### 1. Clone this repo:
```bash
git clone https://github.com/yourusername/resume-review-bot.git
cd resume-review-bot
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set your OpenRouter API key (optional but recommended):
```bash
set OPENROUTER_API_KEY=your_key_here  # on Windows
# or
export OPENROUTER_API_KEY=your_key_here  # on Linux/Mac
```

### 4. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## ✅ Example Questions Answered

- Is education mentioned clearly?
- Are skills listed properly?
- What should I add to improve this resume?

---

> 🔧 Built with ❤️ by **Nikhil Basanwal**
