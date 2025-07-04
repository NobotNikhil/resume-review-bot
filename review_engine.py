import os
import requests
import json

def analyze_resume(text):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return rule_based_review(text)

    prompt = f"""
You are a professional resume reviewer and extractor.
Given this resume, return:

1. A structured JSON with:
- full_name
- email
- phone
- education: list of degrees + institutes
- skills: list
- projects: list
- experience: list

2. Then provide feedback on:
- Formatting
- Missing sections
- Suggestions to improve impact

Resume:
{text}
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://openrouter.ai",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        result = res.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error using GPT model: {e}\nFallback feedback:\n" + rule_based_review(text)


def rule_based_review(text):
    feedback = []
    if "education" not in text.lower():
        feedback.append("❗ Education section is missing or unclear.")
    if "experience" not in text.lower():
        feedback.append("❗ Experience section is missing or too weak.")
    if "skill" not in text.lower():
        feedback.append("❗ Skills are not mentioned properly.")
    if "project" not in text.lower():
        feedback.append("❗ Projects not found, consider adding some.")
    if len(text) < 500:
        feedback.append("❗ Resume content is too short. Add more relevant details.")

    structure = {
        "full_name": "Not detected",
        "email": "Not found",
        "phone": "Not found",
        "education": [],
        "skills": [],
        "projects": [],
        "experience": []
    }

    return json.dumps({
        "structured_resume": structure,
        "feedback": feedback or ["Resume format looks good."]
    }, indent=2)
