time = str(input('Enter time in 24 hour format: '))

time12 = time.split(':')

hour = int(time12[0])

if hour > 12:
    hour = hour - 12
    print (f'The time is {hour}:{time12[1]}pm')
else:

    print(f'The time is {hour}:{time12[1]}am')