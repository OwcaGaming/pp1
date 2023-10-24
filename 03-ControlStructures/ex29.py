washing_product = "jacket"
time = 0
rinse = True
spin = False

if washing_product == "Shoes":
    time += 20

if washing_product == "jacket":
    time += 40
    
if washing_product == "underwear":
    time += 70

if rinse == True:
    time += 15
if spin == True:
    time += 9
    
print(f'The wash time is {time} minutes')