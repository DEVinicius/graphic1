# -*- coding: utf-8 -*-
import tkinter
import PySimpleGUI as sg

class PythonScreen:
    #definição das variaveis iniciais dentro da classe
    def __init__(self):
        # Layout
        layout = [
            #criação de Label e Input
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Email'), sg.Input()],
            [sg.Button("Enviar")]
        ]
        # Janela
        window = sg.Window("User Data", layout)
        # Extração de dados
        self.button, self, values = window.Read()
    
    def Start(self):
        print(self.values)

tela = PythonScreen()
tela.Start()