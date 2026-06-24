def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes)/60)
def main():
    user_time=input("What time is it? ").strip()
    current_hour=convert(user_time)
    if 7.0 <= current_hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= current_hour <= 13.0:
        print("lunch time")
    elif 18.0 <= current_hour <= 19.0:
        print("dinner time")
if __name__ == "__main__":
    main()

