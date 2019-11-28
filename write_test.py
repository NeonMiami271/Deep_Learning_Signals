import csv

data = ['Headphones', '$7.05', '$11.00' ,'$4.00']

with open('write_test.csv', 'wt') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(('Item', 'Cost', 'Sold', 'Profit'))
    writer.writerow(data)