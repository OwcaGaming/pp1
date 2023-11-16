def acronym(text):
    text = str(text)
    acro = ''
    if text[0] != ' ':
        acro = text[0]
    for i in range (1, len(text)):
        if text[i-1] == ' ':
            acro += text[i]
    return acro

print (acronym(' For Your Information'))