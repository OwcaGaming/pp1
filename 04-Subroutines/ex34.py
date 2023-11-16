def string_numbers(number):
    text = ''
    
    i = 0
    while i <= number:
        text = f'{text}'+f'{i}'
        i+=1
    return text
        
        
print (string_numbers(13))
        