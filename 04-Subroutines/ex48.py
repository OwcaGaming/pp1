def product_number(number):
    number = list(str(number))
    first3 = 0
    for i in range(0, 3):
        first3 += int(number[i])
    if first3%7 == int(number[3]):
        return True
    else:
        return False
    
print(product_number(1082))
