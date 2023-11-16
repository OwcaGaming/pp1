def card_number(num):
    num = str(input('Enter card number: '))
    encrypted = str()
    for i in range (0, 16):
        if i < 2 or 11 < i < 16:
            encrypted += num[i]
        else:
            encrypted += "*"
    return encrypted
num = ()
print(card_number(num))
            
        
    