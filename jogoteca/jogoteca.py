from flask import Flask, render_template, request, redirect

from models.game import Game

app = Flask(__name__)

game1= Game('Tetris', 'Puzzle', 'Atari')
game2= Game('God of War', 'Rack n Slash', 'PS2')
gameList = [game1, game2]

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', title="Jogos", games=gameList)

@app.route('/form-new-game')
def form_new_game():
    return render_template('form-new-game.html', title="Adicionar novo jogo")

@app.route('/add-game', methods=['POST',])
def add_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    gameList.append(game)
    return redirect('/')

app.run(debug=True)