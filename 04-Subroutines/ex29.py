def amount_to_pay(amount):
    amount = int(input('Enter amount: '))
    count = 0 
    while amount >= 5:
        amount -= 5
        count +=1
    while amount >= 2:
        amount -= 2
        count +=1
    while amount >= 1:
        amount -= 1
        count +=1
    return count
n = 0
if __name__ == "__main__":
    print(amount_to_pay(n))