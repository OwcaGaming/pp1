star = str(' * ')
length = int(input('Enter length: '))

for i in range (1, length + 1):
    if i <= (length+1)/2 :
        print(star*i)
    else:
        print(star*(length-i+1))