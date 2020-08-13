#!/usr/bin/env python3
import tkinter
from Screen import Screen
from Csv import CSV

screen = Screen()
csv = CSV()
file_path = screen.Start()

csv_file = csv.CsvVerify(file_path)

if csv_file == False:
    exit()
else:
    screen.SecondScreen(csv.OpenCsv(csv_file))
    
