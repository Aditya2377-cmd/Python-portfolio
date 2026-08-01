import sys


def main():
    check_command_line_args()
    filename = sys.argv[1]
    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                stripped_line = line.strip()
                if stripped_line != "" and not stripped_line.startswith("#"):
                    count += 1

            print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_command_line_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
