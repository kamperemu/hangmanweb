from flask import Flask, render_template, request, redirect
from game import gameUI, reset

app = Flask(__name__)
guess = ""
game = ""
guessed = []
word = ""
noGuess = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/word', methods=['GET', 'POST'])
def word():
    global word
    global guessed
    if request.method == 'POST':
        word,guessed = reset()
        word = request.form['word'].lower()
        return redirect('/game')
    else:
        return render_template('word.html')
        


@app.route('/game', methods=['GET', 'POST'])
def game():
    global noGuess
    global word
    global guess
    global game
    global guessed
    if request.method == 'POST':
        guess = request.form['letter']
        return redirect('/game')
    else:
        game, noGuess = gameUI(word, guess, guessed, noGuess)
        if game == word or noGuess>=8:
            return render_template('winorlose.html', word=word, winorlose='WIN' if game == word else 'LOSE')
            word,guessed = reset()
        else:
            return render_template('game.html', game=game, noGuess=noGuess)


if __name__ == "__main__":
    app.run(debug=True)
