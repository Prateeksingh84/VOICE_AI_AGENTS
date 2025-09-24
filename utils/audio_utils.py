import os
import pyttsx3

def generate_sample_audio(filename="sample.wav", male_voice=True):
    os.makedirs("data", exist_ok=True)
    text = (
        "Hello, my name is Prateek Singh. "
        "I have three years of experience in Python and AI. "
        "I am based in Bangalore and can join immediately."
    )
    path = os.path.join("data", filename)

    engine = pyttsx3.init()
    
    # List available voices
    voices = engine.getProperty('voices')
    
    # Male voice is usually index 0, female is index 1 (platform-dependent)
    engine.setProperty('voice', voices[0].id if male_voice else voices[1].id)
    
    engine.save_to_file(text, path)
    engine.runAndWait()
    return path
