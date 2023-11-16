def range(x, y):
    count = 0
    i = x
    while i <= y:
        if i < 0 and i%2 == 0:
            count +=1
        i += 1
    return count

print(range(2, 10))