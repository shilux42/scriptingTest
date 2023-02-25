import csv

with open ('NQ Monday 1813.csv') as f:
    reader = csv.reader(f, delimiter = ';')
    for line in reader:
        print(line)

data = [
    [1, 2, 3]
    [4, 5, 6]
]

with open ('out.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(data)