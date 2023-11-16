def dice_rolled(num):
    num = str(num)
    check = 0
    number = 0
    for i in range (1, 7):
        if num.count(f'{i}') > check:
            check = num.count(f'{i}')
            number = i
    return number
print(dice_rolled(5551222234))