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
# print(soup.prettify())

# CSS-Selektor für die Auslastung
css_selector = '#main > div.main-content-body.pt-0 > div.container.container--narrow.mb-5 > div.capacity-bar > div.capacity-bar__percent'
# Selektor von Firefox
# .capacity-bar__percent

# CSS-Selektor für die Auslastung
css_selector_temp = 'li.d-none:nth-child(1) > a:nth-child(1) > span:nth-child(2)'
# X-Path
# /html/body/div[3]/div/nav/ul/li[1]/a/span
# CSS-Selektor für die Pisten-KM
css_selector_km = 'li.d-none:nth-child(3) > a:nth-child(1) > span:nth-child(2)'
# CSS-Selektor für die Anlagen
css_selector_lifte = 'li.d-none:nth-child(6) > a:nth-child(1) > span:nth-child(2)'

# Auslastung extrahieren
auslastung = soup.select_one(css_selector).text.strip()
# Temperatur extrahieren
temperatur = soup.select_one(css_selector_temp).text.strip()
# temperatur = 0
# Pisten-KM extrahieren
# kilometer = soup.select_one(css_selector_km).text.strip()
kilometer = 0
# Geoeffnete Lifte extrahieren
# lifte = soup.select_one(css_selector_lifte).text.strip()
lifte = 0

# Unerwünschte Symbole entfernen
# auslastung = auslastung.replace('%', '').strip()

print(f"Kapazität: {auslastung}")

# Aktuelles Datum und Uhrzeit erfassen
jetzt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Daten in einer CSV-Datei speichern
csv_dateiname = 'ausgabe.csv'
with open(csv_dateiname, mode='a', newline='', encoding='utf-8') as datei:
    csv_writer = csv.writer(datei)
    # Spaltenüberschriften hinzufügen
    csv_writer.writerow(['Datum und Uhrzeit', 'Auslastung', 'Temperatur', 'Pisten-KM', 'Anlagen'])
    # Daten hinzufügen
    csv_writer.writerow([jetzt, auslastung, temperatur, kilometer, lifte])

print(f'Daten wurden erfolgreich in {csv_dateiname} gespeichert.')
