def operations(operation):
    operation = list(str(operation))
    sum = int(operation[0])
    for i in range(0, len(operation)):
        if operation[i] == '+':
            sum += int(operation[i+1])
        if operation[i] == '-':
                sum -= int(operation[i+1])
    return sum

print(operations('2+3-4+5-0'))