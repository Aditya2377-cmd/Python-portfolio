import tabulate
import csv
import sys

new=[]
try:
    with open(sys.argv[1]) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
        table.append(row)
        print(tabulate(table,headers="firstrows",tablefmt="grid"))
except FileNotFoundError:
    pass
