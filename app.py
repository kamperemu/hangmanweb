from flask import Flask, render_template, request, redirect
from game import gameUI

app = Flask(__name__)
guess = ""
game = ""
guessed=[]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods = ['GET','POST'])
def game():
    global guess
    global game
    if request.method == 'POST':
        guess = request.form['letter']
        return redirect('/game')
    else:
        game = gameUI(guess,guessed)
        return render_template('game.html', game=game)

if __name__ == "__main__":
    app.run(debug=True)