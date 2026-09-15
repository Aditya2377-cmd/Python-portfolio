import random
def main():
    user1 = get_level()
    score = 0
    ops = { "A" : "Addition" , "S" : "Subtraction" , "M" : "Multiplication", "D" : "Division"}
    operation = get_op()

    for i in range(10):
        score = generate_integer(user1, score, operation)

    print(f"Score: {score}")

def get_op():
    while True:
        try:
            innet = input("Enter the operation you want to test with : ")
            if innet in ops:
                return innet
            print(f"You have chosen : {ops[innet]}")



def get_level():
    while True:
        try:
            iret = int(input("Level: "))
            if iret in [1, 2, 3, 4, 5]:
                 return iret
        except ValueError:
            pass

def generate_integer(level, score):
    if level == 1:
        start, end = 0, 9
    elif level == 2:
        start, end = 10, 99
    elif level == 3:
        start, end = 100,999
    elif level == 4:
        start, end = 1000,9999
    else:
        start, end = 10000, 99999

    if

    inet1 = random.randint(start, end)
    inet2 = random.randint(start, end)
    correct = inet1 + inet2

    tries = 0

    while True:
        try:
            final = int(input(f"{inet1} + {inet2} = "))
            if final != correct:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{inet1} + {inet2} = {correct}")
                    return score
                continue
            else:
                if tries == 0:
                    score += 1
                return score

        except ValueError:
            print("EEE")
            tries += 1
            if tries == 3:
                print(f"{inet1} + {inet2} = {correct}")
                return score
            continue

if __name__ == "__main__":
    main()
