def Convert(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct

def split(word): 
    return [char for char in word] 


word = str(input("Enter the word:"))

word = split(word)


for i in word:
    print("_", end=" ")

