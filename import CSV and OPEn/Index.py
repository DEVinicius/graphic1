from Screen import Screen
from Csv import CSV

screen = Screen()
csv = CSV()
file_path = screen.Start()

separator = csv.CsvVerify(file_path)
print(separator)
