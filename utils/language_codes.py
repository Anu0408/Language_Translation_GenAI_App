#language_codes.py

# Example dictionary for supported languages
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Russian": "ru",
    "Kannada": "ka",
    "Telugu": "te",
    "Hindi": "hi"
    # Add more languages here
}

# You might want to also have a reverse mapping in case it's needed
REVERSE_LANGUAGES = {v: k for k, v in LANGUAGES.items()}
