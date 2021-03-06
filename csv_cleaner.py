import csv

with open('racd.csv', mode='r') as csv_file, open('racd_cleaned.csv', mode='w') as out_file:
    csv_reader = csv.DictReader(csv_file)
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_count = 0
    empty_arrest_rows_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            csv_writer.writerow(row)
            line_count += 1
        else:
            if row["arrested"] == 'N' or row["arrested"] == 'Y':
                to_write = []
                for key,val in row.items():
                    to_write.append(val)
                csv_writer.writerow(to_write)
            else:
                empty_arrest_rows_count += 1
            line_count += 1

    print(f'Processed {line_count} lines.')
    print(f'{empty_arrest_rows_count} emty lines.')
