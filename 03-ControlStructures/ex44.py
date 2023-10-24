i = 0
mean = 0
count = 0
while i < 1:
    num = int(input('Enter number: '))
    if num == 0:
        break
    else:
        mean += num
        count +=1
        
print(f'Quantity={count}, sum={mean}, Mean={mean/count}')