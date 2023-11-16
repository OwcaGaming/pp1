def number_even(num):
    even = False
    check = 0
    sum = 0

    if even == True:
        for i in range (0, len(num)):
            check = int(num[i])
            if check %2 == 0:
                sum += check
               
    else:
        for i in range (0, len(num)):
            check = int(num[i])
            if check %2 > 0:
                sum += check
    return sum
                
num = str(input('Enter number: '))
print(number_even(num))
                
    
            
            

        
        
    