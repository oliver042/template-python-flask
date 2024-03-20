from flask import Flask, render_template, url_for
import csv
import os

# Flask-App initialisieren
app = Flask(__name__)

# Bootstrap CSS lokal speichern
bootstrap_css = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'
os.system(f'wget {bootstrap_css} -O ./static/bootstrap.min.css')

@app.route('/')
def home():
    # Render der Startseite mit Bootstrap
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    # Hier würde der Scraping-Code eingefügt werden
    return 'Scraping gestartet!'

@app.route('/auslastung')
def auslastung():
    # CSV-Datei lesen und Daten für die Tabelle vorbereiten
    daten = []
    with open('ausgabe.csv', mode='r', encoding='utf-8') as datei:
        csv_reader = csv.reader(datei)
        for zeile in csv_reader:
            daten.append(zeile)
    return render_template('auslastung.html', daten=daten)

if __name__ == '__main__':
    app.run(debug=True)
