from faster_whisper import WhisperModel

from faster_whisper import WhisperModel

def transcribe(audio_path):
    # Ensure path is valid and file is closed before use
    if hasattr(audio_path, "name"):
        audio_path = audio_path.name

    model = WhisperModel("base", device="cpu")
    segments, _ = model.transcribe(audio_path)
    text = "".join([seg.text for seg in segments])
    return text.strip()
