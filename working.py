import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex pattern to validate and capture time components
    pattern = r"^([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Convert hours to integer
    h1 = int(h1)
    h2 = int(h2)

    # Validate hour ranges (1 to 12)
    if h1 < 1 or h1 > 12 or h2 < 1 or h2 > 12:
        raise ValueError("Invalid hour")

    # Set default minutes to "00" if None
    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    # Convert to 24-hour format
    time1 = format_24(h1, m1, p1)
    time2 = format_24(h2, m2, p2)

    return f"{time1} to {time2}"


def format_24(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{minute}"


if __name__ == "__main__":
    main()
