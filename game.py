import requests

def check_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    if requests.get(url).status_code == 200:
        return True
    return False

class Game:

    def __init__(self, word, noGuess=8):
        self.word = word.lower()
        self.noGuess = noGuess
        self.guessed = []

    # function: shows how much progress the player has made
    def guessUI(self):
        self.guessStr = ""
        for letter in self.word:
            if letter in self.guessed:
                self.guessStr += letter
            else:
                self.guessStr += "_"

    # function: finds number of guesses left
    def guessLeft(self):
        return self.noGuess - len(self.guessed)

    # function: appends player's guess
    def playerGuess(self, guess):
        guess = guess.lower()
        if guess not in self.guessed:
            self.guessed.append(guess)

    # function: that checks if game is won
    def isWin(self):
        if str(self) == self.word:
            return True
        return False

    # function: that checks if game loop should continue
    def continueGameLoop(self):
        if self.isWin() or self.noGuess <= len(self.guessed):
            return False
        return True

    # function: that generates string
    def __str__(self):
        self.guessUI()
        return self.guessStr

if __name__ == "__main__":
    word = input("Enter Word:")
    if check_word(word):
        newGame = Game(word, 8)
    while newGame.continueGameLoop():
        guess = input("> ")
        if len(guess) == 1:
            newGame.playerGuess(guess)
        print(str(newGame))
    if newGame.isWin():
        print(f"You Win! The word is {newGame.word}")
    else:
        print(f"You Lose! The word is {newGame.word}")

