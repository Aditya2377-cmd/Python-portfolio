# Get and split the input into three parts
expr = input("Expression: ").strip()

# Add spaces around the operator if they are missing
for op in ["+", "-", "*", "/"]:
    if op in expr and f" {op} " not in expr:
        expr = expr.replace(op, f" {op} ")

x, y, z = expr.split()

# Check the operator and print the result formatted to 1 decimal place
if y == "+":
    print(f"{float(x) + float(z):.1f}")
elif y == "-":
    print(f"{float(x) - float(z):.1f}")
elif y == "*":
    print(f"{float(x) * float(z):.1f}")
elif y == "/":
    print(f"{float(x) / float(z):.1f}")


