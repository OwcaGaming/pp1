num = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum = 0
for i in range(0,4):
    for j in range(0,3):
       if num[i][j]%2 != 0:
           sum += num[i][j]
print(sum) 