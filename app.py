# app.py
import gradio as gr
from transcriber import transcribe
from intent_classifier import get_intent
from output_generator import generate_output

def process_audio(audio_file):
    try:
        text = transcribe(audio_file)
        print("📝 Transcription:", text)

        intent = get_intent(text)
        print("📌 Intent Detected:", intent)

        result = generate_output(intent, text)
        print("📤 Generated Output:", result)

        return f"📝 Transcription:\n{text}\n\n📌 Detected Intent: {intent}\n\n✉️ Generated Output:\n{result}"
    except Exception as e:
        import traceback
        print("❌ ERROR:", traceback.format_exc())
        return f"❌ An error occurred:\n{str(e)}"



iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Record Your Voice"),
    outputs=gr.Textbox(label="🧠 AI Response"),
    title="INTENTIFY - From Voice to Action in Seconds",
    description="Speak your message — AI transcribes it, detects intent, and generates an email/reminder/tweet etc."
)

if __name__ == "__main__":
    iface.launch()
