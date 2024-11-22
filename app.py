import gradio as gr
import speech_recognition as sr
import pyttsx3
from models.hugging_face import load_model, translate_text as hug_face_translate
from models.llama_translation import translate_text as llama_translate
from models.libre_translate import libre_translate

# Dictionary of full language names to language codes
language_dict = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Japanese": "ja",
    "Chinese": "zh",
    "Hindi": "hi"
}

# List of full language names for the dropdown
languages = list(language_dict.keys())

# List of translation models to choose from
models = ["Hugging Face", "Llama 3.2", "LibreTranslate"]

# Function to handle translation based on model choice
def translate_text_opusmt(sentence, source_lang, target_lang, model_choice):
    source_lang_code = language_dict[source_lang]
    target_lang_code = language_dict[target_lang]
    
    if model_choice == "Hugging Face":
        # Hugging Face translation model
        model, tokenizer = load_model(source_lang_code, target_lang_code)
        return hug_face_translate(sentence, source_lang_code, target_lang_code, model, tokenizer)
    
    elif model_choice == "Llama 3.2":
        # Llama translation model
        return llama_translate(sentence, source_lang, target_lang, model_choice)
    
    elif model_choice == "LibreTranslate":
        # LibreTranslate API
        return libre_translate(sentence, source_lang_code, target_lang_code)

# Function to handle voice input (STT)
def listen_for_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            # Using Google's speech recognition
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Sorry, there was an issue with the speech recognition service."

# Function to speak the translated text (TTS)
def speak_text(text):
    engine = pyttsx3.init()
    
    # Get available voices
    voices = engine.getProperty('voices')
    
    # Set the voice to a female one (you can experiment with indices for different voices)
    for voice in voices:
        if 'female' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    # Set speech rate and volume (optional)
    engine.setProperty('rate', 150)  # Adjust speed of speech
    engine.setProperty('volume', 1)  # Adjust volume (0.0 to 1.0)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()


# Function to handle translation after recognizing speech
def voice_to_translation():
    # First, listen for the input
    sentence = listen_for_input()
    
    # If recognition fails, return an error
    if "Sorry" in sentence:
        return sentence, ""  # return error message in the output_text
    
    # Now, update the sentence input field with the recognized sentence
    sentence_input.value = sentence  # Correct way to update the value
    
    # Now, translate the recognized sentence
    source_lang = "English"  # Assuming default source language as English
    target_lang = "Spanish"  # Choose the target language or allow dynamic selection
    model_choice = "Hugging Face"  # Choose model as per the requirement
    
    translated_text = translate_text_opusmt(sentence, source_lang, target_lang, model_choice)
    
    return sentence, translated_text  # Return both the recognized and translated text

# Gradio interface
with gr.Blocks() as iface:
    # Adding the app name and a short description
    with gr.Row():
        gr.Markdown(
            """
            <h1 style="text-align:center; color:#4a90e2; font-size: 40px; font-family: 'Arial', sans-serif;">Language Translation App</h1>
            <p style="text-align:center; font-size: 18px; color:#888888; font-family: 'Arial', sans-serif;">Hi! I'm Anu, this app allows you to translate text between multiple languages. You can choose from different translation models like Hugging Face, Llama 3.2, or LibreTranslate to get your translation done!</p>
            """
        )

    # Creating a stylish row with inputs and dropdowns
    with gr.Row():
        sentence_input = gr.Textbox(label="Sentence to Translate", placeholder="Enter text here...", lines=2, interactive=True, elem_id="sentence-input")  # Text input for sentence
        source_lang_input = gr.Dropdown(choices=languages, label="Source Language", interactive=True, elem_id="source-lang-input")  # Dropdown for source language
        target_lang_input = gr.Dropdown(choices=languages, label="Target Language", interactive=True, elem_id="target-lang-input")  # Dropdown for target language
        model_choice_input = gr.Dropdown(choices=models, label="Choose Translation Model", interactive=True, elem_id="model-choice-input")  # Dropdown for model choice
    
    # Add a styled translation button
    translate_button = gr.Button("Translate", elem_id="translate-btn")
    voice_input_button = gr.Button("Speak Sentence", elem_id="voice-input-btn")  # Button for voice input
    voice_output_button = gr.Button("Speak Translation", elem_id="voice-output-btn")  # Button for speaking translation
    
    output_text = gr.Textbox(label="Translated Text", elem_id="output-text", lines=5, interactive=False)  # Output box for translation

    # Apply CSS styling directly to the app using HTML
    gr.HTML(""" 
    <style>
        #sentence-input {
            background-color: #f9f9f9;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 16px;
            padding: 10px;
        }
        #source-lang-input, #target-lang-input, #model-choice-input {
            background-color: #f9f9f9;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 16px;
            padding: 10px;
        }
        #translate-btn {
            background-color: #4a90e2;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 12px 30px;
            border-radius: 8px;
            border: none;
        }
        #translate-btn:hover {
            background-color: #357abd;
        }
        #output-text {
            background-color: #f9f9f9;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 16px;
            padding: 10px;
        }
    </style>
    """)

    # Define button actions
    translate_button.click(
        fn=translate_text_opusmt,
        inputs=[sentence_input, source_lang_input, target_lang_input, model_choice_input],
        outputs=output_text
    )
    
    # Speak sentence button action
    voice_input_button.click(
        fn=voice_to_translation,
        outputs=[sentence_input, output_text]  # Update both sentence input and translated text
    )

    # Speak translation button action
    voice_output_button.click(fn=lambda x: speak_text(x), inputs=output_text)

# Launch the Gradio app
iface.launch(share=True)
