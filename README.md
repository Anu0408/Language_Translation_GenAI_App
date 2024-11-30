# **Language Translation GenAI App**

This Language Translation App allows you to translate text and speech between multiple languages. It uses three different models: **Hugging Face**, **Llama 3.2**, and **LibreTranslate**, for translating text, with options for voice input and output.


## Features
- **Multi-Language Support**: Translate between languages such as English, Spanish, French, German, and more.
- **Multiple Translation Models**: Choose from Hugging Face, Llama 3.2, or LibreTranslate.
- **Voice Translation**: Speak a sentence, and the app will convert it to text and translate it to the target language.
- **Text-to-Speech**: Hear the translated text spoken back to you.

--- 

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/language-translation-app.git
   cd language-translation-app
2. Create a virtual environment: `python -m venv env`
3. Install dependencies: `pip install -r requirements.txt`
4. Set Hugging Face token for Hugging Face models: `token = "your_hugging_face_token"`
5. Run the app: `python app.py`


## Usage
- Text Translation: Enter a sentence, choose languages, and click "Translate".
- Voice Translation: Click "Speak Sentence", and the app will listen and translate your spoken sentence.
- Speak Translation: After translation, you can click "Speak Translation" to hear the translated text.

## Models
- **Hugging Face**: Uses MarianMT from Hugging Face for translation.
- **Llama 3.2**: Uses the Ollama API for Llama 3.2 translations.
- **LibreTranslate**: Uses the LibreTranslate API.as English, Spanish, French, German, and more.






