num = input('Enter registation number: ')

areacode = num[:2]

check = areacode == 'KR' or areacode == 'KK'

print(check)
