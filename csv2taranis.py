import csv
import json

# Pfad zur CSV-Datei und zur Ausgabedatei
csv_file_path = 'csv/institutions_variations_all.csv'
json_file_path = 'output_institutions_variations_all.json'

# Funktion zum Bereinigen von ungültigen Zeichen und Entfernen des BOM
# leider bei excel csv exporten oft vorhanden
def clean_text(text):
    # Entferne BOM, falls vorhanden
    if text.startswith('\ufeff'):
        text = text[1:]
    return text

# Funktion zum Lesen der CSV-Datei und Erstellen der JSON-Daten
def csv_to_json(csv_file_path, json_file_path):
    entries = set()  # Verwende eine Menge, um doppelte Einträge zu vermeiden

    with open(csv_file_path, mode='r', encoding='utf-8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            for cell in row:
                cleaned_cell = clean_text(cell)
                if cleaned_cell.strip():  # Ignoriere leere Zellen
                    entries.add(cleaned_cell.strip())  # Füge den Eintrag zur Menge hinzu

    data = {
        "version": 1,
        "data": [
            {
                "name": "Health",
                "description": "Health",
                "usage": 4,
                "link": "https://raw.githubusercontent.com/kiwimartin/taranis-lists/main/health.json",
                "entries": [{"value": entry, "category": "Einrichtungen"} for entry in entries]  # Konvertiere die Menge in eine Liste von Einträgen
            }
        ]
    }

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Aufruf der Funktion zur Konvertierung
csv_to_json(csv_file_path, json_file_path)
