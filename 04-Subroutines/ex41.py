def prime_number(n):
    count = 0
    isprime = 0
    i = 1
    
    while count < n:
        for j in range(1, i+1):
            if i%j == 0:
                isprime += 1
        if isprime <= 2 and i != 1:
            
            count +=1
        isprime = 0
        i += 1
    return i-1
        
print(prime_number(5))    