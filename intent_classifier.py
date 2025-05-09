import subprocess
import re

def get_intent(text):
    prompt = f"""
You are an intent classifier.

Choose ONLY ONE from the following:
- email
- reminder
- tweet
- note
- blog

Classify this input:
"{text}"

✅ Respond with ONLY ONE WORD (no extra text, punctuation, or quotes). If unsure, choose the closest match.
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode(),
            capture_output=True,
            timeout=30,
        )

        output = result.stdout.decode().strip().lower()
        print("🧠 Raw Intent Output:", output)

        # Strict match: extract only the first valid keyword
        allowed_intents = {"email", "reminder", "tweet", "note", "blog"}
        for word in re.findall(r'\b\w+\b', output):
            if word in allowed_intents:
                return word

        return "note"  # fallback

    except Exception as e:
        print("❌ Intent detection failed:", str(e))
        return "note"
