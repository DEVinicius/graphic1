from Screen import Screen
from Csv import CSV

screen = Screen()
csv = CSV()
file_path = screen.Start()

separator = csv.CsvVerify(file_path)
if separator == True:
    print(f"Arquivo OK")
else:
    print(f"Arquivo não aceito")
