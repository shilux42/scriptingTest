import csv

row_list = []

def parse_row(row):
    row_list.append(row)

def csv_reader(datafile, date, time):
    with open (datafile) as f:
        reader = csv.reader(f, delimiter = ';')
        for pos, row in enumerate(reader):
            #print(row)
            if pos > 0:
                if row[0] == date:
                    if row[1] == time:
                        parse_row(row)
                        print(row_list)

if __name__ == '__main__':
    with open ('out.csv', 'w') as f:
        date = '06/01/2020' #input('Enter the date (dd/mm/yyyy): ')
        time = '00:00:00' #input('Enter the time (00:00): ')
        csv_reader('NQ Monday 1813.csv', date, time)
        writer = csv.writer(f)
        writer.writerow(row_list)