import requests

def elevenlabs_speak(text, voice="Rachel"):
    url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": "TU_API_KEY",
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