from bs4 import BeautifulSoup
import requests

# URL der Webseite
url = 'https://www.ischgl.com/de/Active/Active-Winter/Skifahren/Pisten-Anlagen'

# Anfrage an die Webseite senden
response = requests.get(url)

# HTML-Inhalt parsen
soup = BeautifulSoup(response.content, 'html.parser')

# Kapazitätsinformationen extrahieren
capacity_bar = soup.select_one('#main > div.main-content-body.pt-0 > div.container.container--narrow.mb-5 > div.capacity-bar > div.capacity-bar__percent')
capacity_percentage = capacity_bar.text.strip()

print(f"Kapazität: {capacity_percentage}")
