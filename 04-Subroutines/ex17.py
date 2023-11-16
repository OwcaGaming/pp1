def different(n1,n2,n3):
    

    if n1 != n2 != n3:
        return True

n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
n3 = int(input('Enter number 3: '))

if different(n1, n2, n3):
  print(f'The numbers {n1}, {n2} and {n3} are different')
else:
    print('Some numbers are the same')
