pin = "0805"
i = 0   
check = 0

while i < 3:
    
    if check == 3:
        print("too many failed attempts!")
        break
    
    user = str(input('Enter pin: '))
    
    if user == pin:
            print('The pin is correct!')
            break
  
    else:
        print('The pin is incorrect')
        check += 1
        
   
    