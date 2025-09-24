import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_AUDIO = DATA_DIR / "raw"
TRANSCRIPTS = DATA_DIR / "transcripts"
OUTPUTS = BASE_DIR / "outputs"

# Ensure folders exist
for folder in [RAW_AUDIO, TRANSCRIPTS, OUTPUTS]:
    folder.mkdir(parents=True, exist_ok=True)
