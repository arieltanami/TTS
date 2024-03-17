import sys
from pydub import AudioSegment


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
    
    # Convert mono audio to stereo
    audio = AudioSegment.from_file(output_file, format="mp3")
    stereo_audio = audio.set_channels(2)
    stereo_audio.export(output_file, format="mp3")


# main
language = 'en'
text = "text here"
output_file = "output.mp3"

generate_speech(text, language, slow=False, output_file=output_file)