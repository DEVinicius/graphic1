import csv

class CSV:
    def CsvVerify(self,csv):
        separator = csv.split(".")
        for separator_field in separator:
            if separator_field == separator[(len(separator) - 1)]:
                if separator_field == "csv":
                    return csv
                else:
                    return False

    def OpenCsv(self, csv_file):
        with open(csv_file, newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['street'], row['city'], row['zip'], row['state'])
