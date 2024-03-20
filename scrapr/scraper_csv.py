import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL der Ziel-Website
url = 'https://www.ischgl.com/de/Active/Active-Winter/Skifahren/Pisten-Anlagen'

# Anfrage an die Website senden und Antwort erhalten
response = requests.get(url)

# BeautifulSoup-Objekt erstellen, um die HTML-Daten zu parsen
soup = BeautifulSoup(response.text, 'html.parser')

# CSS-Selektor für die Auslastung
css_selector = '#main > div.main-content-body.pt-0 > div.container.container--narrow.mb-5 > div.capacity-bar > div.capacity-bar__percent'

# Auslastung extrahieren
auslastung = soup.select_one(css_selector).text.strip()

# Unerwünschte Symbole entfernen
# auslastung = auslastung.replace('%', '').strip()

print(f"Kapazität: {auslastung}")

# Aktuelles Datum und Uhrzeit erfassen
jetzt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Daten in einer CSV-Datei speichern
csv_dateiname = 'ausgabe.csv'
with open(csv_dateiname, mode='w', newline='', encoding='utf-8') as datei:
    csv_writer = csv.writer(datei)
    # Spaltenüberschriften hinzufügen
    csv_writer.writerow(['Datum und Uhrzeit', 'Auslastung'])
    # Daten hinzufügen
    csv_writer.writerow([jetzt, auslastung])

print(f'Daten wurden erfolgreich in {csv_dateiname} gespeichert.')
