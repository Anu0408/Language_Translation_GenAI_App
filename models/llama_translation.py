#llama_translation.py

from langchain_ollama.llms import OllamaLLM
import requests



# Function to translate text using Llama 3.2 model (OllamaLLM)
def translate_text(sentence, source_language, target_language, model_choice):
    if model_choice == "Llama 3.2":
        try:
            # Initialize Ollama model with llama3.2
            model = OllamaLLM(model="llama3.2")
            
            # Construct the prompt for translation
            prompt = f"Translate the following text from {source_language} to {target_language}: {sentence}"
            
            # Get the response from the model
            response = model(prompt)
            
            # Returning the response from the model
            return response.strip() if response else "Error: No response from Llama model."
        except Exception as e:
            return f"Error during Llama translation: {str(e)}"
    
    
