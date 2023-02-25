import csv

data = []

def parse_row(row):
    data.append(row)

with open ('NQ Monday 1813.csv') as f:
    reader = csv.reader(f, delimiter = ';')
    for pos, row in enumerate(reader):
        #print(row)
        if pos > 0:
            if row[0] == '20/10/2022':
                if row[1] == '08:00:00':
                    parse_row(row)
                    


print(data)


with open ('out.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(data)