def count_numbers(num):

    text = list(str(num))
    all = 0

    for i in range (1, 10):
        if text.count(f'{i}') > 1:
            all += text.count(f'{i}')*i
    return all        
        
    
    
print(count_numbers(513553007))
