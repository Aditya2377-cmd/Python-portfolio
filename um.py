import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # \b captures word boundaries so "yummy" or "album" are ignored
    # re.IGNORECASE makes it match "um", "Um", "UM", etc.
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
