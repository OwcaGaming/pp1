def remove_space(text):
    splittext = text.split()
    removed = ''
    i=0
    while i < len(splittext):
        removed += splittext[i]
        i += 1
    return removed
    

print(remove_space('you are cute'))

