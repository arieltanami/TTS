import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "gtts"])

from gtts import gTTS

def generate_speech(text: str, language: str, slow: bool, output_file: str) -> None:
    """
    Generate speech from the given text and save it as an audio file.

    Args:
        text (str): The text to convert to speech.
        language (str): The language of the text (e.g., 'en' for English).
        slow (bool): Whether to generate speech at a slower speed.
        output_file (str): The path to save the generated audio file.

    Returns:
        None
    """
    speech = gTTS(text=text, lang=language, slow=slow)
    speech.save(output_file)


# main
language = 'en'
text = "text here"
output_file = "text.mp3"

generate_speech(text, language, slow=False, output_file=output_file)