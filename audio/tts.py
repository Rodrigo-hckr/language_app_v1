from audio.elevenlabs_api import elevenlabs_speak

def speak(original, translation):
    elevenlabs_speak(original)
    elevenlabs_speak(translation)