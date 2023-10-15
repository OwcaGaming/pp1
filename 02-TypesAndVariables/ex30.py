import random

user = int(input('Guess the number: '))

ran = random.randrange(1, 7)

check = ran == user

print(f'Was the right number? {check}')