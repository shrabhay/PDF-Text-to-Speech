import fitz
from google.cloud import texttospeech
from dotenv import load_dotenv
import os

load_dotenv()
client = texttospeech.TextToSpeechClient.from_service_account_file(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

pdf_file = 'sample.pdf'
speech_file = 'output.mp3'


def get_text_from_pdf_file(pdf):
    text = ''
    doc = fitz.open(pdf)
    for page in doc:
        text += page.get_text()
    return text


def split_text(text, max_bytes=5000):
    chunks = []
    current_chunk = ''
    for paragraph in text.split('\n'):
        if len(current_chunk.encode('utf-8')) + len(paragraph.encode('utf-8')) < max_bytes:
            current_chunk += paragraph + '\n'
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


def text_to_speech(text):
    for idx, text in enumerate(text):
        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=input_text,
            voice=voice,
            audio_config=audio_config
        )

        mode = 'wb' if idx == 0 else 'ab'
        with open(speech_file, mode) as file:
            file.write(response.audio_content)


pdf_text = get_text_from_pdf_file(pdf=pdf_file)
text_chunks = split_text(text=pdf_text)
text_to_speech(text=text_chunks)
