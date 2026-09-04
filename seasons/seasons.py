import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    user_input = input("Date of Birth: ")
    try:
        minutes = get_minutes(user_input, date.today())
        print(f"{convert_to_words(minutes)} minutes")
    except ValueError:
        sys.exit("Invalid date")

3
def get_minutes(dob_str, today_date):
    dob = date.fromisoformat(dob_str)
    difference = today_date - dob
    total_minutes = difference.days * 24 * 60
    return total_minutes


def convert_to_words(time):
    words = p.number_to_words(time)
    words = words.replace(" and " , " ")
    return words.capitalize()


if __name__ == "__main__":
    main()
