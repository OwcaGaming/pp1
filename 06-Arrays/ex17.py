num = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    num[i][i] = 1

display = ''
for x in range(0,3):
    for y in range(0,3):
        display += f'{num[x][y]} '
    print(display)
    display = ''