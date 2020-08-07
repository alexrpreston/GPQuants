import csv
with open('/Users/alexpreston/Downloads/test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    result = ""
    for row in csv_reader:
        singleRow = "('" + row[1] + "', '" + row[1] + " - " + row[0] + "'),"
        result = result + str(singleRow) + "\n"

    print(result)
