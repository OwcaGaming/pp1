def letter_e():
    sentence = str(input('Enter sentence: '))
    n = 0 
    check = 0
    while n <= len(sentence)-1:
        if sentence[n] == "e":
            check += 1
        
        n += 1
    
    
    return check
