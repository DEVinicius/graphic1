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
        window = sg.Window("CSV OPEN", layout, size=(1000,100), element_justification = 'center')

        self.button, self.values = window.Read()
        window.Close()

    def Start(self):
        csv_file_path = self.values["csv_file"]
        return csv_file_path

    def SecondScreen(self, csv):
        #layout
        layout = [
            [sg.Text("Dados do Arquivo Csv")],
            [sg.popup_scrolled(csv)],
        ]

        window = sg.Window("CSV SHOW", layout, size=(1000,100), element_justification = 'center')

        self.button, self.values = window.Read()