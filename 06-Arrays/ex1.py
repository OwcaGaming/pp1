numbers = ['2','3','7','5','4']
n = ''

for i in range (0, len(numbers)//2+1):
    if i < 1:
       n += numbers[i]
    else:
        n += " " + numbers[i]
print(n)