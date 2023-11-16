numbers = [34,7,19,4,21,8]
sum = 0

for i in range (0, len(numbers)):
    if numbers[i]%2 == 0:
       sum += 1
print(sum)
sum = 0
j = 0
while j < len(numbers):
    if numbers[j]%2 == 0:
        sum += 1
    j += 1
print (sum)