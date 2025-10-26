Norwegian:

# Akademiet Kantine Flask nettside

## Kort beskrivelse av prosjektet

Dette prosjektet er en enkel Flask-basert nettside for Akademiets kantine.  
Nettsiden viser ukens meny, varer til salgs, og kontaktinformasjon for kantinen.  
Prosjektet er laget for å demonstrere grunnleggende bruk av Flask, HTML-templating med Jinja2, og CSS-layout.

## Prosjekt Struktur

Static
    css
        style.css
    images
        (Alle Bildene Brukt)
templates
    base.html
    index.html
    kontakt.html
    meny.html
    varer.html
app.py
README.md
 
### Hjemmeside (`/`)
Viser en introduksjon til kantinen.
Forklarer kort hva nettsiden brukes til.

### Meny (`/meny`)
Viser ukens meny i en ryddig tabell-lignende layout.
Hver rad inneholder dag, dagens rett og et bilde.

### Varer (`/varer`)
Viser produkter som selges i kantinen (f.eks. toast, drikke).
Hver vare har bilde, navn og pris i en egen boks.

### Kontakt (`/kontakt`)
Viser kontaktpersoner for kantinen.
Hver kontaktboks viser navn, e-post, telefonnummer og bilde.

### Teknologi brukt

Python 3
Flask
HTML + Jinja2 
CSS

## Hvordan Kjøre Prosjektet

For å kjøre Flask-appen riktig, bør du bruke et virtuelt miljø.
Et virtuelt miljø gjør at du installerer Flask bare for dette prosjektet, uten å påvirke resten av systemet.

Gjør dette i prosjektmappen der app.py ligger: først oppretter du et virtuelt miljø ved å kjøre python -m venv venv. deretter aktiverer du miljøet på macOS/Linux: source venv/bin/activate, du vil da se (venv) i terminalprompten som viser at miljøet er aktivt. når miljøet er aktivt installerer du Flask kun i dette miljøet med pip install flask, så starter du applikasjonen med python app.py og i terminalen bør du få en melding som: Running on http://127.0.0.1:5000/ åpne denne adressen i nettleseren for å se siden. når du er ferdig kan du slå av miljøet med deactivate.

python -m venv venv
source venv/bin/activate
pip install flask
python app.py

## Utviklet av

Sebastian
Prosjektet er laget som en del av et skoleprosjekt ved Akademiet.

English:

# Akademiet Cantine Flask Website

## Short Project Description

This project is a simple Flask-based website for Akademiet's cantine.
The website shows the weekly menu, items for sale, and contact information for the cantine.
The project is designed to demonstrate basic usage of Flask, HTML templating with Jinja2, and CSS layout.

## Project Structure

Static
  css
    style.css
  images
    (all used images)
templates
  base.html
  index.html
  kontakt.html
  meny.html
  varer.html
app.py
README.md

### Homepage (/)

Displays an introduction to the cantine.
Briefly explains the purpose of the website.
### Menu (/meny)
Shows the weekly menu in a tidy, table-like layout.
Each row contains the day, the dish of the day, and an image.
### Items (/varer)
Shows products sold at the cantine (e.g., toast, drinks).
Each item has an image, name, and price inside its own box.
### Contact (/kontakt)
Shows the cantine's contact persons.
Each contact box displays the name, email, phone number, and picture.

## Technologies Used

Python 3
Flask
HTML + Jinja2
CSS

How to Run the Project

To run the Flask app correctly, you should use a virtual environment.
A virtual environment ensures that Flask is installed only for this project without affecting your global Python setup.

In the project folder where app.py is located, first create a virtual environment by running python -m venv venv. Then activate the environment: on macOS/Linux, use source venv/bin/activate. You will then see (venv) in the terminal prompt, indicating that the environment is active. While the environment is active, install Flask using pip install flask. Start the application by running python app.py, and the terminal should display: Running on http://127.0.0.1:5000/
Open this address in your browser to view the site. When you are finished, you can deactivate the environment using deactivate.

python -m venv venv
source venv/bin/activate
pip install flask
python app.py

## Developed By

Sebastian
This project was created as part of a school project at Akademiet.