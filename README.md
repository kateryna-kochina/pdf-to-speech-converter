# PDF to Speech Converter

This Python script converts text from a PDF file into speech using the `PyPDF2` library to get text from PDF file and `gTTS` library and CLI tool to interface with Google Translate's text-to-speech API.

## Prerequisites

Make sure you have the required libraries installed:

```
pip install -r requirements.txt
```

## Usage

1. Replace 'your_pdf_file.pdf' with the path to your PDF file in the pdf_file_path variable.
2. Run the script:

```
python pdf_to_speech_converter.py
```

3. The script will extract text from the PDF and convert it into speech. The audio file will be saved as output.mp3 by default.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute, report issues, or suggest improvements!
