 months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    while True:
        try:
            user_input = input("Date: ").strip()
            if "/" in user_input:
                month, day, year = user_input.split("/")
                if month.isalpha():
                    continue
            elif "," in user_input:
                month_name, day, year = user_input.split(" ")
                day = day.replace(",", "")
                if month_name in months:
                    month = months[month_name]
                else:
                    continue

            else:
                continue
            if int(month) > 12 or int(day) > 31:
                continue
            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break
        except ValueError:
            continue
