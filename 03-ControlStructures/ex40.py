sentence = str(input('Enter sentence: '))
i = 0
space = str()
while i < len(sentence):
    space = space + " " + sentence[i] + " "
    i += 1
    
print (space)