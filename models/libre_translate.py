# Libre_translate.py

import requests

def libre_translate(sentence, source_language, target_language):
    """
    Translate text using LibreTranslate.

    Args:
        sentence (str): The text to translate.
        source_language (str): Source language code (e.g., "en").
        target_language (str): Target language code (e.g., "te").
    
    Returns:
        str: Translated text or error message.
    """
    url = "https://libretranslate.com/translate"
    payload = {
        "q": sentence,
        "source": source_language,
        "target": target_language,
        "format": "text"
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()["translatedText"]
    else:
        return f"Error: {response.text}"







# Function to translate text using LibreTranslate API (hosted or public)
def libre_translate(sentence, source_language, target_language):
    url = "https://libretranslate.com/translate"  # Public API endpoint
    payload = {
        "q": sentence,
        "source": source_language,
        "target": target_language,
        "format": "text"
    }
    
    try:
        # Sending request to LibreTranslate
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            # Returning translated text
            return response.json()["translatedText"]
        else:
            # Returning error message if response is not 200
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"