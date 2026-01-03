from googletrans import Translator
from pykakasi import kakasi
from pypinyin import lazy_pinyin
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from transliterate import translit as ru_translit
import pyttsx3

# Disable TTS as per your request
def speak(text):
    pass  # You can enable it later if needed

def translate_text(text, dest_language='ta'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def transliterate_to_english(native_text, lang_code):
    lang_map = {
        'hi': sanscript.DEVANAGARI,
        'ta': sanscript.TAMIL,
        'te': sanscript.TELUGU,
        'kn': sanscript.KANNADA,
        'ml': sanscript.MALAYALAM,
        'bn': sanscript.BENGALI,
        'gu': sanscript.GUJARATI,
        'pa': sanscript.GURMUKHI,
    }

    try:
        if lang_code in lang_map:
            return transliterate(native_text, lang_map[lang_code], sanscript.ITRANS)
        elif lang_code == 'ru':
            return ru_translit(native_text, 'ru', reversed=True)
        elif lang_code in ['zh-cn', 'zh-tw']:
            return ' '.join(lazy_pinyin(native_text))
        elif lang_code == 'ja':
            kakasi_obj = kakasi()
            result = kakasi_obj.convert(native_text)
            return ' '.join([item['hepburn'] for item in result])
        elif lang_code in ['fr', 'es', 'de', 'ar']:
            return "(pronunciation approximation not available)"
        else:
            return "(pronunciation not supported)"
    except Exception as e:
        return f"(pronunciation error: {str(e)})"

# Main execution block (runs once and exits)
if __name__ == "__main__":
    print(" English ➡ Native + Pronunciation\n")

    text = input("Enter English sentence: ")
    lang_code = input("Enter target language code (hi, ta, te, kn, ml, bn, gu, pa, ru, zh-cn, ja, fr, es, de, ar): ")

    try:
        native = translate_text(text, dest_language=lang_code)
        pronunciation = transliterate_to_english(native, lang_code)

        print(f"\n Output:\n{native} - {pronunciation}")
        speak(native)
    except Exception as e:
        print(" Error:", e)

    
