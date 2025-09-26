import json

def load_phrases(plan):
    file_map = {
        "basic": "data/frases_basicas.json",
        "extended": "data/frases_practicas.json",
        "full": "data/frase_polyglot.json"
    }
    path = file_map.get(plan, file_map["basic"])
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)