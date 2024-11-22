#translator.py

import requests
from models.llama_translation import translate_text as llama_translate

def translate(sentence, source_language, target_language, model_choice):
    if model_choice == "Llama 3.2":
        # Call the Llama 3.2 translation function
        return llama_translate(sentence, source_language, target_language)
    elif model_choice == "Libre Translate":
        # Call the Libre Translate API (assuming it is running locally on port 5000)
        url = "http://localhost:5000/translate"
        response = requests.post(url, data={
            'q': sentence,
            'source': source_language,
            'target': target_language
        })
        if response.status_code == 200:
            return response.json().get('translatedText', 'Error: Translation failed')
        else:
            return f"Error: Unable to translate with LibreTranslate. Status code: {response.status_code}"
    else:
        return "Invalid Model Choice"
