def main():
    print(validate(input("IPv4 Address: " )))

def validate(ip):
    while True:
        try:
            one, two, three, four = ip.split(".")
            if one <255:
                print("True")
            elif one <0:
                print("False")
            elif one.isalpha():
                print("False")
            elif one == 255:
                print("True")
            else:
                print("False")

        except ValueError:
            pass

if __name__ == "__main__":
    main()

