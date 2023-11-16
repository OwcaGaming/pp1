def sentence(text):
    text = list(str(text))
    
    for i in range (1, len(text)*2-1, 2):
        text.insert(i, '-')
    return ''.join(str(x) for x in text)
        
print(sentence(''))