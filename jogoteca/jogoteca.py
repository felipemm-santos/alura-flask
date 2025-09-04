import os
from flask import Flask, flash, render_template, request, redirect, session

from models.game import Game

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

game1= Game('Tetris', 'Puzzle', 'Atari')
game2= Game('God of War', 'Rack n Slash', 'PS2')
gameList = [game1, game2]

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', title='Jogos', games=gameList)

@app.route('/new-game')
def new_game():
    if 'logged_user' not in session or session['logged_user'] is None:
        return redirect('/login?next=new-game')
    else:
        return render_template('new-game.html', title='Adicionar novo jogo')

@app.route('/add-game', methods=['POST',])
def add_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    gameList.append(game)
    return redirect('/')

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', title='Login', next=next)
    
@app.route('/authentication', methods=['POST',])
def authentication( ):
    if 'rtm' == request.form['password']:
        session['logged_user'] = request.form['username']
        flash('Usuário logado com sucesso', 'success')
        next_page = request.form['next']
        return redirect('/{}'.format(next_page) if next_page else '/')
    else:
        flash('Usuário ou senha incorretos. Tente novamente', 'error')
        return redirect('/login')
    

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Usuário deslogado com suceso', 'success')
    return redirect('/')

app.run(debug=True)