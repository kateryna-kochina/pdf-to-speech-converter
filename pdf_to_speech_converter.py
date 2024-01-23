import PyPDF2
from gtts import gTTS


def pdf_to_text(pdf_path):
    '''
    Convert text from a PDF file to a string.

    Parameters:
    - pdf_path (str): Path to the PDF file.

    Returns:
    str: Extracted text from the PDF.
    '''
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def text_to_speech(text, output_file='output.mp3', language='en'):
    '''
    Convert text to speech and save it as an audio file.

    Parameters:
    - text (str): Input text to convert to speech.
    - output_file (str, optional): Output file path for the audio file. Default is 'output.mp3'.
    - language (str, optional): Language for text-to-speech conversion. Default is 'en'.

    Returns:
    str: Path to the saved audio file.
    '''
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    return output_file


if __name__ == '__main__':
    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_file_path = 'your_pdf_file.pdf'

    # Convert PDF to text
    pdf_text = pdf_to_text(pdf_file_path)

    # Convert text to speech
    output_audio_file = text_to_speech(pdf_text)

    print(f'Text from PDF has been converted to speech. Audio file saved as: {output_audio_file}')
