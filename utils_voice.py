import os
import uuid
from gtts import gTTS
from io import BytesIO

VOICE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'voices')
os.makedirs(VOICE_DIR, exist_ok=True)

LANG_MAP = {
    'vi': 'vi',
    'en': 'en',
    'ko': 'ko',
    'ja': 'ja',
    'zh': 'zh',
    'fr': 'fr',
    'de': 'de',
    'es': 'es',
    'th': 'th',
}

def generate_voice(text: str, lang: str = 'vi') -> dict:
    try:
        lang_code = LANG_MAP.get(lang, 'vi')
        tts = gTTS(text=text, lang=lang_code)
        
        filename = f"voice_{uuid.uuid4().hex[:12]}.mp3"
        filepath = os.path.join(VOICE_DIR, filename)
        tts.save(filepath)
        
        return {
            "success": True,
            "filename": filename,
            "url": f"/static/voices/{filename}"
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
