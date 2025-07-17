from transformers import pipeline

def translate_text(text, source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    
    try:
        translator = pipeline("translation", model=model_name)
        result = translator(text)
        return result[0]['translation_text']
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("🌐 Language Translator using AI")
    
    text = input("Enter text to translate: ")
    source = input("Enter source language code (e.g., en, fr, de, es): ")
    target = input("Enter target language code (e.g., en, fr, de, es): ")

    if source == target:
        print("Source and target languages must be different.")
    else:
        translated = translate_text(text, source, target)
        print("✅ Translated Text:", translated)
