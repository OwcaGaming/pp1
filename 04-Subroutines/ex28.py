def binary_number(n):
    n = str(input('Enter number: '))
    i = 0
    while i < len(n):
        if n[i] == "1" or n[i] == "0":
            i +=1
            check = True
        else:
            return False
    if check == True:
            return True
            
            
a = ()
print(binary_number(a))
        