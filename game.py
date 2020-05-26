def Convert(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct

def split(word): 
    return [char for char in word] 



word = str(input("Enter the word:"))

word = split(word)

guessed = []

guess = str(input("Guess a letter: "))

guessed.append(guess)

for i in word:
    letter = False
    for j in guessed:
        if i==j:
            letter = True
    if letter:
        print(i, end = " ")
    else:
        print("_", end=" ")

