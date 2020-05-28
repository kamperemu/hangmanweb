def guessUI(word,guessed):
    guessUI=""
    for i in word:
        letter = False
        for j in guessed:
            if i==j:
                letter = True
        if letter:
            guessUI+=i
        else:
            guessUI+="_"
    return guessUI




def split(word): 
    return [char for char in word] 



def gameUI(guess,guessed):
    word="hello"
    wordlist = split(word)
    guessed.append(guess)
    return guessUI(wordlist,guessed)