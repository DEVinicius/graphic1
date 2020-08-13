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
        with open(csv_file,"r") as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ";")
            # line_count = 0
            # for row in spamreader:
            #    # if line_count == 0:
            #     print(f'{"  |".join(row)}')
            #     print("")
            return spamreader
