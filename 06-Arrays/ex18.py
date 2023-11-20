tf = [[True,False],[True,True],[False,False]]
for i in range(0,3):
    for j in range (0,2):
        if tf[i][j] == True:
            tf[i][j] = False
        else:
            tf[i][j] = True
    
print(tf)