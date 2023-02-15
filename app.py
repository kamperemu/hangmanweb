from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from game import Game, check_word

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/word', methods=['GET', 'POST'])
def word():
    if request.method == 'POST':
        word = request.form['word']
        if check_word(word):
            session["Game"] = Game(word)
        else:
            return redirect("/word")
        return redirect('/game')
    else:
        return render_template('word.html')
        


@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        guess = request.form['letter']
        if len(guess) == 1:
            session["Game"].playerGuess(guess)
        return redirect('/game')
    else:
        if not session["Game"].continueGameLoop():
            return render_template('winorlose.html', word=session["Game"].word, winorlose='WIN' if session["Game"].isWin() else 'LOSE')
        else:
            return render_template('game.html', game=str(session["Game"]), noGuess=session["Game"].guessLeft())


if __name__ == "__main__":
    app.run(debug=True)
