import tkinter
import PySimpleGUI as sg

class FileScreen:
    def __init__(self):
        #layout 
        layout = [
            [sg.Text("Arquivo CSV")],
            [sg.Input(key="file_path"), sg.FileBrowse()],
            [sg.Open(), sg.Cancel()]
        ]
        #Window
        window = sg.Window("Import Csv", layout)

        self.button, self.values = window.Read()

    def Start(self):
        file_path = self.values["file_path"]
        print(f"File Name = {file_path}")

file = FileScreen()
file.Start()