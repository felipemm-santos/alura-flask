import os
from dotenv import load_dotenv

from flask import Flask, flash, render_template, request, redirect, session, url_for

from models.game import Game
from models.user import User

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

user1 = User('admin', 'rtm')
user2 = User('user', '123')
userList = {user1.username: user1, user2.username: user2}

game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('God of War', 'Rack n Slash', 'PS2')
gameList = [game1, game2]

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', title='Jogos', games=gameList)

@app.route('/new-game')
def new_game():
    if 'logged_user' not in session or session['logged_user'] is None:
        return redirect(url_for('login', next=url_for('new_game')))
    else:
        return render_template('new-game.html', title='Adicionar novo jogo')

@app.route('/add-game', methods=['POST',])
def add_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    gameList.append(game)
    return redirect(url_for('home'))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', title='Login', next=next)
    
@app.route('/authentication', methods=['POST',])
def authentication( ):
    if 'username' not in request.form or request.form['username'] not in userList:
        flash('Usuário ou senha incorretos. Tente novamente', 'error')
        return redirect(url_for('login'))

    user = userList[request.form['username']]
    
    if user.password == request.form['password']:
        session['logged_user'] = user.username
        flash('Usuário logado com sucesso', 'success')
        next_page = request.form['next']
        return redirect(next_page if next_page else url_for('home'))
    else:
        flash('Usuário ou senha incorretos. Tente novamente', 'error')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Usuário deslogado com suceso', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)