import sys
from pathlib import Path

# Add project root to sys.path so imports work
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.audio_utils import generate_sample_audio
from nlp.analyze import analyze_text
from nlp.live_callback import live_nlp_callback
from utils.scoring_utils import screening_score, summarize_decision

def transcribe_audio_dummy(audio_path):
    """
    Dummy transcript (replace with Whisper ASR for real audio).
    """
    live_nlp_callback("Transcribing audio...")
    return (
        "Hello, my name is Prateek Singh. "
        "I have three years of experience in Python and AI. "
        "I am based in Bangalore and can join immediately."
    )

def print_hr_report(transcript, analysis, score, decision):
    print("\n" + "="*50)
    print("📝 Candidate Screening Report")
    print("="*50)
    print(f"📜 Transcript:\n{transcript}\n")
    print(f"🔑 Keywords: {', '.join(analysis.get('keywords', []))}")
    print(f"🗣️ Tone Score: {analysis.get('tone_score', 0.0)}")
    print(f"📊 Screening Score: {score}")
    print(f"✅ Decision: {decision}")
    print("="*50 + "\n")

def main():
    # 1️⃣ Generate male voice audio
    audio_path = generate_sample_audio(male_voice=True)
    print(f"✅ Generated male voice audio: {audio_path}")

    # 2️⃣ Transcribe audio
    transcript = transcribe_audio_dummy(audio_path)
    print("📜 Transcript:", transcript)

    # 3️⃣ NLP analysis
    analysis = analyze_text(transcript)
    print("🔎 Analysis:", analysis)

    # 4️⃣ Screening score
    score = screening_score(
        skill_match=0.8,
        years=3,
        notice_days=14,
        willingness_score=0.9,
        tone=analysis.get("tone_score", 0.7),
    )
    decision = summarize_decision(score)

    # 5️⃣ Simulated UI card
    ui_card = {
        "Transcript": transcript,
        "Analysis": analysis,
        "Screening Score": score,
        "Decision": decision
    }
    print("💻 Simulated UI Card:", ui_card)

    # 6️⃣ HR-style formatted report
    print_hr_report(transcript, analysis, score, decision)

if __name__ == "__main__":
    main()
