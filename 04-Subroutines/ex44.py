def check_password(password):
    password = str(password)
    i = 0
    
    if len(password) >= 6:
        while i < len(password):
            if password.count(f'{password[i]}') > 1:
                return False
            i+=1        
        return True
            
    else:
        return False
        
print(check_password('1234'))