# misc
def split(word):
    return [char for char in word]


# function: shows how much progress the player has made
def guessUI(word, guessed, noGuess):
    guessUI = ""
    noGuess = len([x for x in guessed if x not in word]) - 1
    for i in word:
        letter = False
        for j in guessed:
            if i == j:
                letter = True
        if letter:
            guessUI += i
        else:
            guessUI += "_"
    return guessUI, noGuess


# function: the game itself
def gameUI(word, guess, guessed, noGuess):
    wordlist = split(word)
    guessed.append(guess)
    game, noGuess = guessUI(wordlist, guessed, noGuess)
    return game, noGuess


# function: resets all variables
def reset():
    guessed = []
    word = ""
    return word, guessed
