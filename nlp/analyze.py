import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

def analyze_text(text: str):
    """
    Extract skills/entities and compute a dummy tone score.
    Returns a dictionary with 'skills' and 'tone_score'.
    """
    doc = nlp(text)
    # Extract entities labeled ORG, PRODUCT, or SKILL
    # Note: spaCy default model doesn't have SKILL label, so we also consider nouns as skills
    skills = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT"]]
    
    # Optional: simple noun chunk fallback
    if not skills:
        skills = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]

    # Dummy tone scoring
    tone_score = 0.8 if "immediately" in text.lower() else 0.6

    return {"skills": skills, "tone_score": tone_score}

# 🔹 Test
if __name__ == "__main__":
    sample_text = "Hello, I have 3 years experience in Python and AI. I can join immediately."
    result = analyze_text(sample_text)
    print("🔎 Analysis Result:", result)
