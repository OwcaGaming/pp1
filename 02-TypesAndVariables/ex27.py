w = float(input('Enter your weight: '))
h = float(input('Enter your height in meters: '))

bmi = w/h**2

check = bmi >= 18.5 and bmi <= 24.9

print (check)