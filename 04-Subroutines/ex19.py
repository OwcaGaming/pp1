import digits

number = int(input('Enter number: '))

sum_d = digits.sum_digits(number)
msg = f'Sum of digits is {sum_d}'
print(msg)