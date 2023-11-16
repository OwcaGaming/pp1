def is_palindrome(sentence):
    if sentence == sentence[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("kajak"))