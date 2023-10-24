num = int(input('Enter number: '))
mod = str('')
div = 0
i = 0
while num > 0:
    if num%2 == 1:
        mod = mod + '1'
    else:
        mod = mod +'0'
    num = num//2
    
    
print(mod[::-1])
