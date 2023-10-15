#num = int(input('Enter binary number: '))
dec = 0
num = str(1001)
numlength = len(num)

for i in range(numlength):
    
    if num[i] == '1':
        dec += 2**(numlength-i-1)
        
print (dec)
