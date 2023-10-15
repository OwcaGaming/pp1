word = input('Enter word: ')
wordlength = len(word)

for i in range(wordlength):

    if i <= wordlength:
        
        print(f"{word[i]} ({ord(word[i])})")


