def people(text):
    check = 0
    
    length = len(text)

    n = 0
    while n < length:
        if text[n] == "+":
            check += 1
        else:
            check -= 1
        if check == 3:
            return True
        else:
            return False


print(people("+-+-+-+-"))