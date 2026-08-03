import csv
import sys

if len(sys.argv)< 3:
    sys.exit("Too less command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command line arguments")
try:
    with open(sys.argv[1],"r") as infile, open(sys.argv[2],"w") as outfile:
        reader =csv.DictReader(infile)
        writer =csv.DictWriter(outfile, fieldnames= ["first", "last", "house"])

        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({"first": first.strip(),
                            "last": last.strip(),
                            "house":row["house"]})
except FileNotFoundError :
    sys.exit("Input does not exist")


