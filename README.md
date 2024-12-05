# PDF to Speech Conversion

This Python project converts the text content of a PDF file into an audio file (MP3) using Google Cloud Text-to-Speech API. It processes large texts by splitting them into smaller chunks to handle API limitations and combines the audio output into a single MP3 file.

---

## Features

- Extracts text from PDF files.
- Converts text to speech using Google Cloud Text-to-Speech API.
- Handles API limitations by splitting large text into manageable chunks (under 5000 bytes).
- Generates high-quality MP3 audio output.

---

## Requirements

To run this project, ensure the following dependencies are installed:

- Python 3.8+
- Required Python libraries:
  - `google-cloud-texttospeech`
  - `pymupdf` (install using `fitz` module)
  - `python-dotenv`
- Google Cloud Service Account JSON key file for Text-to-Speech API.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/shrabhay/PDF-Text-to-Speech.git
   cd PDF-Text-to-Speech

2. Install dependencies

3. Add your Google Cloud service account credentials:

   * Save your JSON key file locally.
   * Create a `.env` file in the project root directory with the following content:
   ```text
    GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
    ```
   
4. Replace the default PDF filename in the script with your desired file.

---

## Usage
1. Place your PDF file in the project directory.

2. Run the script:
    ```commandline
    python tts.py
    ```

3. The script generates an MP3 file (default: output.mp3) in the project directory.

---

## Configuration
* **PDF File**: Replace the pdf_file variable with the name of your PDF file.
* **Output File**: Change the speech_file variable to customize the MP3 output filename.

---

## Error Handling
* **API Limitations**: The script splits the PDF text into chunks under 5000 bytes to comply with Google Cloud Text-to-Speech API limits.
* **Missing Environment Variables**: Ensure the .env file contains the correct path to the JSON key file.

---

## Acknowledgments
* Google Cloud Text-to-Speech API
* PyMuPDF (fitz)
* Python dotenv

---

## License
This project is licensed under the MIT License.

---

## Contribution
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements or bug fixes.