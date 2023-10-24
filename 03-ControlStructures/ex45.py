n = int(input('How many prime numbers to find? '))
isprime = 0
count = 0
i=0
while count < n:
    for j in range (1, i+1):
       if i%j == 0:
           isprime +=1
           
           
    if isprime <= 2:
        print (i)
        count +=1
    isprime = 0
    i+=1
        



     
     