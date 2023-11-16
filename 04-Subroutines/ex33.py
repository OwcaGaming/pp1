def asterisks(n):
    star = "*"
    text = list(star*n)
    print(*text, sep=('/'))
    

print (asterisks(5))    

