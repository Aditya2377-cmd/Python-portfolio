import tabulate
import csv
try:
    with open('sicilian.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        pizza=tabulate.spamreader
        print(pizza)
except FileNotFoundError:
    pass
