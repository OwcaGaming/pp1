minc = int(input('enter mothers income: '))
finc = int(input('enter fathes income: '))
family = int(input ('enter number of people in family: '))

totalinc = minc + finc
incpp = totalinc/family

print(f'Total income: {totalinc}' + f'  Income per person: {incpp}')