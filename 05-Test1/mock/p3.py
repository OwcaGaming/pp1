def f(name):
    acro = name[0]
    name = str(name)
    for i in range (0, len(name)):
        if name[i-1] == " ":
            acro += name[i]
    return acro
if __name__ == "__main__":
    #check your program in this place
   print(f('Hello Poland Krakow university'))