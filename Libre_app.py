#app.py

import streamlit as st
import requests
from models.llama_translation import translate_text  # Assuming llama_translation.py is in the models folder
from utils.language_codes import LANGUAGES
from utils.translator import translate

# Set page title
st.title("Language Translation App")

# Dropdown to choose the source language
source_language = st.selectbox(
    'Select Source Language',
    list(LANGUAGES.keys())
)

# Dropdown to choose the target language
target_language = st.selectbox(
    'Select Target Language',
    list(LANGUAGES.keys())
)

# Dropdown to choose the translation model (Llama 3.2 or Libre Translate)
model_choice = st.selectbox(
    'Choose Translation Model',
    ['Llama 3.2', 'Libre Translate']
)

# Input box to enter sentence for translation
sentence = st.text_area('Enter the Sentence to Translate')

# Translate button
if st.button('Translate'):
    if sentence.strip() != "":
        st.write(f"Source Language: {source_language}")
        st.write(f"Target Language: {target_language}")
        st.write(f"Model Choice: {model_choice}")
        st.write(f"Sentence: {sentence}")
        
        with st.spinner("Translating..."):
            # Call the translate function to get the translated text
            translated_sentence = translate(sentence, source_language, target_language, model_choice)
            st.success(f"Translated Text: {translated_sentence}")
    else:
        st.warning("Please enter a sentence to translate.")
