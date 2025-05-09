from llm_utils import run_llm

def generate_output(intent, transcription):
    if intent == "reminder":
        prompt = f"Write a simple, clear reminder for: '{transcription}'"
    elif intent == "note":
        prompt = f"Create a short internal note based on this: '{transcription}'"
    elif intent == "tweet":
        prompt = f"Generate a concise tweet based on: '{transcription}'"
    elif intent == "blog":
        prompt = f"Write a short blog introduction for: '{transcription}'"
    elif intent == "email":
        prompt = f"Write a formal email based on this message: '{transcription}'"
    else:
        prompt = f"Just rephrase this nicely: '{transcription}'"

    return run_llm(prompt)
