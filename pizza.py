from tabulate import tabulate
import csv
import sys
if len(sys.argv)>2:
    sys.exit("Too many command- line arguments")
elif len(sys.argv)<2:
    sys.exit("Too less command-line arguments")
elif not sys.argv[1].endswith(".csv") or sys.argv[1].startswith("#"):
    sys.exit("Not a csv file")

new=[]
try:
    with open(sys.argv[1]) as jack:
        oggy=csv.reader(jack)
        for row in oggy:
            new.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")
print(tabulate(new,headers="FirstRow",tablefmt="grid"))

