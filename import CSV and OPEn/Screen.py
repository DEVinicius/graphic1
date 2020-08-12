import tkinter
import PySimpleGUI as sg

class Screen:
    def __init__(self):
        #layout
        layout = [
            [sg.Text("Insira o Arquivo CSV")],
            [sg.Input(key="csv_file"), sg.FileBrowse()],
            [sg.Open(), sg.Cancel()]
        ]

        # Window
        window = sg.Window("CSV OPEN", layout)

        self.button, self.values = window.Read()

    def Start(self):
        csv_file_path = self.values["csv_file"]
        return csv_file_path