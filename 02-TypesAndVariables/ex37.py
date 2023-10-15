data = "Mr. John May, born on 1998-02-16"

name = data[4:8]
surname = data[9:12]
initials = data[4] + data[9]
birthdate = data[22:32]

print(f""" Name: {name} 
surname: {surname} 
Initials: {initials} 
Birthdate: {birthdate}""")
