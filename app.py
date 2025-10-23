from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/varer')
def varer():
    varerer = [
        {"navn": "Toast", "pris": 30, "bilde": "/static/images/Toast.jpg"},
        {"navn": "sjokolademelk", "pris": 30, "bilde": "/static/images/sjokolademelk.jpeg"},
        {"navn": "Proteinbar", "pris": 35, "bilde": "/static/images/Proteinbar.webp"}, 
        {"navn": "Cola", "pris": 25, "bilde": "/static/images/Cola.jpg"},
        {"navn": "Eplejuice", "pris": 15, "bilde": "/static/images/eplejuice.jpeg"}
    ]
    return render_template("varer.html", varere=varerer)

@app.route('/meny')
def meny():
    menyer = [
        {"dag": "Mandag", "dagens": "Tomat suppe", "bilde": "/static/images/tomatsuppe.jpeg"},
        {"dag": "Tirsdag", "dagens": "Lasgne", "bilde": "/static/images/lasagne.jpg"},
        {"dag": "Onsdag", "dagens": "Fiske kaker", "bilde": "/static/images/fiskekaker.jpeg"},
        {"dag": "Torsdag", "dagens": "Haifinnsuppe", "bilde": "/static/images/haifinnesuppe.jpg"},
        {"dag": "Fredag", "dagens": "Taco", "bilde": "/static/images/taco.jpeg"}
    ]
    return render_template("meny.html", menyer=menyer)

@app.route('/kontakt')
def kontakt():
    kontakter = [
        {"person": "Sebastian", "email": "sebastian@hotmail.com", "nummer": "+ 47 901 33 902", "bilde": "/static/images/smilieemoji.jpeg"},
        {"person": "Marcus", "email": "marcus@hotmail.com", "nummer": "+ 47 902 44 903", "bilde": "/static/images/smilieemoji.jpeg"}
    ]
    return render_template("kontakt.html", kontakter=kontakter)


if __name__ == '__main__':
    app.run(debug=True)

