import librosa
import numpy as np
from transformers import pipeline

asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def transcribe_audio(file_path, chunk_length_s=10, chunk_callback=None):
    """Transcribe audio in chunks with Whisper pipeline."""
    y, sr = librosa.load(file_path, sr=16000)
    total_duration = librosa.get_duration(y=y, sr=sr)
    transcript = []

    for start in range(0, int(total_duration), chunk_length_s):
        end = min(start + chunk_length_s, int(total_duration))
        chunk = y[start * sr:end * sr]

        if len(chunk) == 0:
            continue

        # Convert to float32 numpy
        if not isinstance(chunk, np.ndarray):
            chunk = np.array(chunk, dtype=np.float32)

        result = asr(chunk)
        text = result["text"]

        if chunk_callback:
            chunk_callback(text)

        transcript.append(text)

    return " ".join(transcript)
