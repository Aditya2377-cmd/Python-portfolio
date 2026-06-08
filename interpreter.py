# Get and split the input into three parts
x, y, z = input("Expression: ").split()

# Check the operator and print the result formatted to 1 decimal place
if y == "+":
    print(f"{float(x) + float(z):.1f}")
elif y == "-":
    print(f"{float(x) - float(z):.1f}")
elif y == "*":
    print(f"{float(x) * float(z):.1f}")
elif y == "/":
    print(f"{float(x) / float(z):.1f}")


