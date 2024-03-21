import requests
from bs4 import BeautifulSoup


# URL der Ziel-Website
url = 'https://www.ischgl.com/de/Active/Active-Winter/Skifahren/Pisten-Anlagen'

# Anfrage an die Website senden und Antwort erhalten
response = requests.get(url)

# BeautifulSoup-Objekt erstellen, um die HTML-Daten zu parsen
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

# Öffnen einer Datei im Schreibmodus. 'output.html' ist der Dateiname.
with open('output.html', 'w', encoding='utf-8') as file:
    # Schreiben des geparsten und formatierten HTML-Codes in die Datei.
    file.write(soup.prettify())

print('Daten gespeichert.')