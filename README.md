### 🧠 Intentify — Voice to Action in Seconds

Intentify is a voice-powered productivity tool that converts your short voice inputs into clear, actionable text — like emails, reminders, tweets, or notes — using open-source LLMs locally via Ollama.

🔥 Features

🎙️ Record voice → automatic transcription with faster-whisper
🧠 Intent detection: email, reminder, tweet, note, blog
📝 Output generation using local LLM (mistral via Ollama)
🌐 Clean Gradio UI (no Streamlit!)
🛠️ 100% local inference, no OpenAI API needed

🚀 Demo
https://github.com/user-attachments/assets/3bc45305-58ff-4a4a-91bf-0740f985ec8a

📦 Tech Stack

### Component               Technology
    Transcription:          faster-whisper
    LLM Inference:          mistral via ollama
    Intent Detection:       Prompt-engineered LLM
    Frontend:               Gradio
    Backend Logic:          Python, subprocess

🛠️ Setup Instructions
1. Clone the repo
```bash
git clone https://github.com/yourusername/intentify.git
cd intentify
```
2. Set up virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows5. Run the App
# OR
source venv/bin/activate  # Linux/macOS
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Install Ollama + Pull Model
```bash
# Install ollama from https://ollama.com
ollama pull mistral
```
5. Run the App
```bash
python app.py
```
Go to http://127.0.0.1:7860 to use it.

🎤 Sample Voice Input

"Remind me to submit the project by 5 p.m. today."
Detected Intent: reminder
Generated Output:
Submit Project by 5 p.m. today

💡 Why This Project?

This is part of my #30DaysOfGenAI challenge — Day 4 — building projects that solve real workflow pain points. Intentify simplifies voice-based task delegation and note-making using fully open-source components.

🙋‍♀️ Let's Connect

Built by Varshitha Yanamala. If you're a recruiter, engineer, or GenAI enthusiast — let’s connect!

   

 

