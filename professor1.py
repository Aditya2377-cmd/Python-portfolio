import random
def main():
    user1=get_level()
    score=0
    for i in range(10):
        user2=generate_integer(user1,score)
def get_level():
    while True:
        try:
            iret = int(input("Level: "))
            if iret in [1, 2, 3]:
               return iret
        except ValueError:
            pass


def generate_integer(level,score):
    if level == 1:
        start, end = 0, 9
    elif level == 2:
        start, end = 10, 99
    else:
        start, end = 100, 999
    inet1=random.randint(1,10)
    inet2=random.randint(1,10)
    correct = inet1 + inet2
    tries = 0
    while True:
            try:
                 final = int(input(f" {inet1} + {inet2} = " ))
                 if final != correct :
                     print("EEE")
                     tries += 1
                     if tries == 3:
                          print(f"{inet1} + {inet2} = {correct}")
                          return score
                     else:
                          if tries == 0:
                               score += 1
                               return score
                          continue
            except ValueError:
                pass

if __name__== "__main__":
    main()

