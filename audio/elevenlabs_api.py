from pydub import AudioSegment
from pydub.playback import play
import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

def elevenlabs_speak(text, voice_id="EXAVITQu4vr4xnSDxMaL"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
         "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        with open("temp_audio.mp3", "wb") as f:
            f.write(response.content) # -> reproducimo con pydub o pygame
        sound = AudioSegment.from_mp3("temp_audio.mp3")
        play(sound)
    else:
        print("Error al generar audio:", response.text)