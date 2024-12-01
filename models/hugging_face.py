#hugging_face.py

from transformers import MarianMTModel, MarianTokenizer
from huggingface_hub import login
import gradio as gr

# Get Hugging Face token from Gradio secrets
token = gr.Secret("hugging")
login(token)

def load_model(source_lang, target_lang):
    """
    Loads the MarianMT model and tokenizer for translation.
    """
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate_text(sentence, source_lang, target_lang, model, tokenizer):
    """
    Translate a sentence using the Hugging Face MarianMT model.
    """
    # Tokenize input sentence
    inputs = tokenizer.encode(sentence, return_tensors="pt", padding=True)
    
    # Perform translation
    translated = model.generate(inputs, max_length=512)
    
    # Decode and return the translated sentence
    return tokenizer.decode(translated[0], skip_special_tokens=True)
