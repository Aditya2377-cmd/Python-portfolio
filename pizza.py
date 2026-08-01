from tabulate import tabulate
import csv
import sys

new=[]
try:
    with open(sys.argv[1]) as jack:
        oggy=csv.reader(jack)
        for row in oggy:
            new.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

