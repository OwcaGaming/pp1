num = [[2,5,4],[9,0,3]]
print(num)
print(f'number of columns: {len(num)} number of rows: {len(num[0])}')
print(num[0][1])
print(num[1][2])
text = ''
for i in range (0,3):
    text = text + f'{num[1][i]} '
print(text)
