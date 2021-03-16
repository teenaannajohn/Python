import csv
with open('D:\csvfile.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)