def main():
    print(validate(input("IPv4 Address: " )))

def validate(ip):
    one,two,three,four = ip.split(".")
    if one > 0 and one <= 255 and not one.isalpha:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

