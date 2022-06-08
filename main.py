import requests
from flask import Flask, render_template, request

def get_w():
    url = "https://danepubliczne.imgw.pl/api/data/synop/station/kasprowywierch"
    r = requests.get(url)
    content = r.json()
    return content

d = get_w().get('data_pomiaru')
g = get_w().get('godzina_pomiaru')
s = get_w().get('stacja')
t = get_w().get('temperatura')
o = get_w().get('suma_opadu')

print(" Lokalizacja: "+s+"\n","Data: "+d+"\n","Godzina: "+g+":00\n","Temperatura: "+t+"\n","Opady w mm: "+o+"\n")

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html', s=s, d=d, g=g, t=t, o=o)

app.run()
