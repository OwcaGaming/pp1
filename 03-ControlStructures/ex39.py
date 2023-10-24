a = 4
b = 15
star = str('*')
space = str(' ')

for i in range(1, 5):
    if i == 1 or i == 4:
        print(star*b)
    else:
        print(star + space*(b-2) + star)