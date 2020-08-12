class CSV:
    def CsvVerify(self,csv):
        separator = csv.split(".")
        for separator_field in separator:
            if separator_field == separator[(len(separator) - 1)]:
                if separator_field == "csv":
                    return True
                else:
                    return False