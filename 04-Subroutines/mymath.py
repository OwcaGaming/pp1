import random

def generate_number(ran):
    ran = random.randint(1, 9)
    return (ran)
    
if __name__ == "__main__":
    print(generate_number())