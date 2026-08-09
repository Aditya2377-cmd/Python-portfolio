def main():
    print(validate(input("IPv4 Address: " )))

def validate(ip):
    one = ip.split(".")
    if len(ip) != 4:
        return False
    for part in one:
        if not part.isdigit():
            return False
        if  not ( 0 <= int(part) <= 255):
            return False
        return True


if __name__ == "__main__":
    main()

