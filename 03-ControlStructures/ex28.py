num = str(input("Enter EAN - 13 number: "))

if len(num) == 13:
    print('The number is correct')
    if num[0:3] == '590':
        print('Article maufactured in Poland')
        
        