from auth.user import User
from plans.access import get_plan_features
from phrases.loader import load_phrases 
from audio.tts import speak
from ui.app import launch_app

def main():
    print("Bienvenido a LanguageAPP v0")
    username = input("ingresa tu nombre: ")
    plan = input("selecciona tu plan (Gratis, Practice, Polyglot): ")
    
    user = User(username, plan)
    features = get_plan_features(plan)
    phrases = load_phrases(features["access"])
    
    for i, item in enumerate(phrases):
        print(f"{i+1}. {item['original']} -> {item['translation']}")
        play = input("¿Escuchar esta frase? (s/n): ")
        if play.lower() == "s":
            speak(item["original"], item["translation"])
            
        fav = input("¿Guardar como favorita? (s/n): ")
        if fav.lower() == "s":
            user.add_favorite(item)
            
    print("\nTus frases Favoritas:")
    for phrase in user.favorites:
        print(f"- {phrase['original']} -> {phrase['translation']}")
        
if __name__ == "__main__":
    launch_app()