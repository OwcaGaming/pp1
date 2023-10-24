facebook = input('Do u have facebook? (Y/N): ')
instagram = input('Do u have ig? (Y/N): ')
twitter = input('Do u have twitter? (Y/N): ')
total = 0

if facebook == 'Y':
    total += 1
if instagram == 'Y':
    total += 1
if twitter == 'Y':
    total += 1
if total >= 2:
    print(' u can be a good influencer')
else:
    print('No influencing for u ')