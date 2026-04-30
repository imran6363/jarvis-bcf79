import requests
from config import OPENAI_API_KEY
from core.brain import offline_ai

def online_ai(cmd):
    if not OPENAI_API_KEY:
        return "Online AI not configured"

    try:
        res = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": cmd}]
            }
        )
        return res.json()['choices'][0]['message']['content']
    except:
        return "Network error"

def process(cmd):
    offline = offline_ai(cmd)
    if offline:
        return offline

    return online_ai(cmd)
