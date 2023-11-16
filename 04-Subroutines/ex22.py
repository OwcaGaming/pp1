import mymath
import mykeyboard
n=0

check1 = mymath.generate_number()
check2 = mykeyboard.read_number(n)

if check1 == check2:
    print('U won!')
    
else:
    print('You lost!')
