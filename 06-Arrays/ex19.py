import random
arr1 = []
arr2 = [[],[],[]]
arr3 = []
arr4 = []
arr5 = []

arr1.insert(0, 3)
arr1.insert(1, 7)
arr1.insert(2, 1)
arr1.insert(3, 0)
arr1.insert(4, 4)

arr2[0].insert(0, 2)
arr2[0].insert(1,3)
arr2[1].insert(0,7)
arr2[1].insert(1,1)
arr2[2].insert(0,0)
arr2[2].insert(1,4)

for i in range(7):
    arr3.insert(i, 5)
    
for j in range (1, 10):
    arr4.insert(j, j)

for x in range(10):
    arr5.insert(x, random.randint(1,20))
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)