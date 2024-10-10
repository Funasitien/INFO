from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Hinshala La Clef Hyper Secure WTF'

tab = ([0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
      )

@app.route('/')
def home():
    w = 0
    Game = '<div><p>┌────┬────┬────┬────┬────┬────┬────┐<br>'
    for table in tab:
        w = w + 1
        ligne = f"│"
        for child in table:
            if child == 0:
                ligne = ligne + "‎‎ "
            if child == 1:
                ligne = ligne + " ⭐️ "
            if child == 2:
                ligne = ligne + " 🗿️ "
            ligne = ligne + "│"
        Game =  Game + ligne + "<br>"
        if w == 6:
            Game =  Game + '└────┴────┴────┴────┴────┴────┴────┘<br>0️⃣    1️⃣    2️⃣    3️⃣    4️⃣    5️⃣    6️⃣   <br></p></div>'
        else:
            Game =  Game + '├────┼────┼────┼────┼────┼────┼────┤<br>'
    return Game