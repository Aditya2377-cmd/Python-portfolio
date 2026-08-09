import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regex checks for:
    # 1. <iframe tag at start or within HTML
    # 2. src=" attribute containing http(s)://(www.)youtube.com/embed/VIDEO_ID"
    pattern = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"'

    match = re.search(pattern, s)

    if match:
        return f"https://youtu.be/{match.group(1)}"

    return None


if __name__ == "__main__":
    main()
