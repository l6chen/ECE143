import csv
with open('/Users/nickchen/Desktop/age_searched_cor.csv', mode='r') as in_file, open('/Users/nickchen/Desktop/age_searched_cleaned.csv', mode='w') as out_file:
    csv_reader = csv.DictReader(in_file)
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_count = 0
    empty_arrest_rows_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            csv_writer.writerow(row)
            line_count += 1
        else:
            if (row["searched"] == 'Y' or row["searched"] == 'N') and len(row["subject_age"]) == 2 and row["subject_age"] !='No Age':
                to_write = []
                for key,val in row.items():
                    to_write.append(val)
                csv_writer.writerow(to_write)
            else:
                empty_arrest_rows_count += 1
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(f'{empty_arrest_rows_count} emty lines.')
import csv
with open('/Users/nickchen/Desktop/gender_searched_cor.csv', mode='r') as in_file, open('/Users/nickchen/Desktop/gender_searched_cleaned.csv', mode='w') as out_file:
    csv_reader = csv.DictReader(in_file)
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_count = 0
    empty_arrest_rows_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            csv_writer.writerow(row)
            line_count += 1
        else:
            if (row["searched"] == 'Y' or row["searched"] == 'N') and (row["subject_sex"] == 'M' or row["subject_sex"] == 'F') :
                to_write = []
                for key,val in row.items():
                    to_write.append(val)
                csv_writer.writerow(to_write)
            else:
                empty_arrest_rows_count += 1
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(f'{empty_arrest_rows_count} emty lines.')
