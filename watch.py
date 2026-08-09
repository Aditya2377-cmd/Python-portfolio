import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Search for the pattern inside string 's'
    pattern = r'https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)'

    match = re.search(pattern, s)

    # If a match was found:
    if match:
        # match.group(1) gives the text captured inside the parentheses ()
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    # If no match found, return None
    return None


if __name__ == "__main__":
    main()
