import subprocess
import json

def run_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        if result.returncode != 0:
            print("LLM error:", result.stderr.decode("utf-8"))
            return "⚠️ LLM generation failed. Check Ollama model."

        output = result.stdout.decode("utf-8").strip()
        return output

    except subprocess.TimeoutExpired:
        return "⚠️ LLM timeout. Try a shorter input."

    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"
