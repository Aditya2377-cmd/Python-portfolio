while True:
    fuel = input("Fraction: ").strip()
    try:
        x_str, y_str = fuel.split("/")
        x = int(x_str)
        y = int(y_str)
        if x > y:
            continue
        percentage = round((x / y) * 100)
        break

    except (ValueError, ZeroDivisionError):
        pass
if 0<percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

