import csv
 
FILENAME = "write_test.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:

    	print(','.join(row))	