def live_nlp_callback(text: str):
    """
    Prints live NLP processing updates.
    """
    print(f"🗣️ Live NLP Processing: {text}")


# 🔹 Test code
if __name__ == "__main__":
    live_nlp_callback("Transcribing audio...")
    live_nlp_callback("Analyzing keywords...")
    live_nlp_callback("Calculating screening score...")
    live_nlp_callback("Generating report...")   
    live_nlp_callback("Process completed.")
