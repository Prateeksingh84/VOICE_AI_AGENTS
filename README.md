# 🤖 Voice AI Agent – Automated Candidate Screening

## 📌 Overview

The **Voice AI Agent** is an automated system designed to screen job candidates via **telephonic conversations**. It can:

* Generate or receive **voice audio**
* **Transcribe** the audio using AI models
* Perform **NLP analysis** on candidate responses
* Calculate **screening scores**
* Deliver a **final decision** (Advance, HR Review, Reject)
* Simulate **HR-style UI reports**

This pipeline is ideal for **HR teams**, **recruiters**, or **training purposes**.

## 🚀 Key Features

* 🎤 Real-time **audio transcription** (Whisper / Hugging Face)
* 🔍 **NLP analysis** to extract skills, tone, and keywords
* 📊 **Automated scoring** based on experience, skill match, availability, and tone
* 💻 **Simulated UI card** for easy viewing of candidate data
* 📝 **Formatted HR-style reports** for candidate evaluation
* 🔁 Easily extendable for **multiple candidates**

## 🏗️ Folder Structure

```
voice-ai-agent/
├── src/
│   ├── main.py                # Main execution script
│   ├── nlp/
│   │   ├── analyze.py         # Text analysis
│   │   └── live_callback.py   # Live NLP updates
│   ├── utils/
│   │   ├── audio_utils.py     # Audio generation / handling
│   │   └── scoring_utils.py   # Scoring & decision functions
├── data/
│   └── sample.wav             # Sample audio file
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

* **Python 3.10+**
* `spaCy` – NLP and entity extraction
* `transformers` / `Whisper` – Speech-to-text
* `librosa` – Audio processing
* Base Python libraries: `os`, `sys`, `json`
* Optional: `pyttsx3` for generating male/female voice

## 🔁 Workflow Steps

1. **Generate or load audio** – You can create a male/female voice sample or use an existing file.
2. **Transcribe audio** – Converts speech to text (dummy transcription in example).
3. **NLP analysis** – Extracts keywords, skills, and tone score.
4. **Screening score calculation** – Combines skill match, experience, notice period, willingness, and tone into a score.
5. **Decision making** – Determines if candidate should advance, be reviewed, or rejected.
6. **Simulated UI & HR report** – Prints all relevant candidate info in readable format.

## 📦 How to Run

### 1️⃣ Install dependencies:

```bash
pip install spacy librosa pyttsx3
python -m spacy download en_core_web_sm
```

### 2️⃣ Run the main script:

```bash
python src/main.py
```

### 3️⃣ Output will include:
* Transcript
* Extracted keywords
* Tone score
* Screening score
* HR-style decision

## 🧾 Example Output

```
✅ Generated male voice audio: data/sample.wav
🗣️ Live NLP Processing: Transcribing audio...
📜 Transcript: Hello, my name is Prateek Singh. I have 3 years of experience in Python and AI. I can join immediately.
🔑 Keywords: Python, AI
🗣️ Tone Score: 0.85
📊 Screening Score: 79
✅ Decision: Advance to Technical Interview
```

## ✅ Advantages

* Fully automated candidate screening
* Reusable for multiple roles and skills
* Extensible to real-time telephonic systems
* Provides structured reports for HR teams

## ⚠️ Notes

* Real transcription requires **Whisper / Hugging Face ASR models**
* Ensure Python dependencies are installed
* Customize scoring logic in `scoring_utils.py` as per company policies

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or support, please reach out via:

* **Email**: your-email@example.com
* **GitHub Issues**: [Create an issue](https://github.com/yourusername/voice-ai-agent/issues)

---

⭐ **Star this repository** if you found it helpful!
