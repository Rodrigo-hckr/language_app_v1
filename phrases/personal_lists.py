import csv

def process_uploaded_file(path):
    import csv
    phrases = []
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                phrases.append({"original": row[0], "translation": row[1]})
    return phrases