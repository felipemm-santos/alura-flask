from flask import Flask, render_template

from models import Jogo

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def home():
    jogo1= Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2= Jogo('God of War', 'Rack n Slash', 'PS2')
    lista = [jogo1, jogo2]
    return render_template('index.html', title="Jogos", jogos=lista)

app.run()