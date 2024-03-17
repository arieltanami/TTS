# Python Text-to-Speech Converter

This is a simple Python script that converts text into speech using the Google Text-to-Speech (gTTS) library.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Running the TTS.py Script](#running-the-ttspy-script)
- [Using the Script](#using-the-script)
- [About gTTS](#about-gtts)
- [Additional Resources](#additional-resources)
- [Disclaimer](#Disclaimer)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed [Python](https://www.python.org/downloads/) >=3.7.
* You have a Windows/Linux/Mac machine.

## Quick Start

### Setting Up a Virtual Environment

Before running the script, it's recommended to set up a virtual environment. This helps to keep the dependencies required by different projects separate by creating isolated Python environments for them.

1. Install the `virtualenv` package if it's not already installed:
```bash
pip install virtualenv
```

2. Navigate to the project directory:
```bash
cd path/to/your/project
```

3. Create a new virtual environment in the project directory:
```bash
python3 -m venv venv
```

4. Activate the virtual environment:
    * On Windows:
    ```bash
    venv\Scripts\activate
    ```
    * On Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

### Installing Dependencies

This project requires the `gTTS` and `pydub` libraries. To install them, make sure you're in the virtual environment and run:

```bash
pip install -r requirements.txt
```

### Running the TTS.py Script

To run the `TTS.py` script, follow these steps:

1. Open the `TTS.py` file in a text editor.

2. Replace the text `"text here"` with the text you want to convert to speech. For example:
```python
text = "Hello, world!"
```

3. Save and close the file.

4. Run the script from the terminal:
```bash
python TTS.py
```

The script will generate an MP3 file named `text.mp3` (or whatever you named your output file) in the same directory. You can play this file to hear the text you entered spoken out loud. The MP3 file is in stereo format.

## Using the Script

The `TTS.py` script converts text into speech using the Google Text-to-Speech (gTTS) library. It takes four arguments:

* `text`: The text to convert to speech.
* `language`: The language of the text (e.g., 'en' for English).
* `slow`: Whether to generate speech at a slower speed.
* `output_file`: The path to save the generated audio file.

You can modify these arguments in the `main` section of the script to customize the output.

## About gTTS

gTTS (Google Text-to-Speech) is a Python library and CLI tool to interface with Google Translate's text-to-speech API. It allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more. It also provides customizable text pre-processors which can, for example, provide pronunciation corrections.

You can install gTTS with pip:
```bash
python TTS.py
```

Here's a quick example of how to use gTTS:
```python
from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')
```
For more information, see the [gTTS documentation](http://gtts.readthedocs.org/).

## Additional Resources

- [Python Documentation](https://docs.python.org/)
- [GitHub Guides](https://guides.github.com/)
- [Virtual Environments in Python](https://docs.python.org/3/tutorial/venv.html)

## Disclaimer

This project is not affiliated with Google or Google Cloud. Breaking upstream changes can occur without notice. This project is leveraging the undocumented Google Translate speech functionality and is different from Google Cloud Text-to-Speech.

## License

This project uses the following license:
* The code in this project is licensed under [MIT License](https://opensource.org/licenses/MIT).
* The gTTS library used in this project is licensed under the [MIT License](https://opensource.org/licenses/MIT).