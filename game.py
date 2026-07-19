import random

while True:
    try:
        level=int(input("Level: "))
        if level > 0:
            break

    except ValueError:
        pass

    target= random.randint(1,level)
    
