# -*- coding: utf-8 -*-
import tkinter
import PySimpleGUI as sg

class PythonScreen:
    #definição das variaveis iniciais dentro da classe
    def __init__(self):
        # Layout
        layout = [
            #criação de Label e Input
            [sg.Text('Nome'), sg.Input(key="nome")],
            [sg.Text('Email'), sg.Input(key="email")],
            [sg.Button("Enviar")]
        ]
        # Janela
        window = sg.Window("User Data", layout)
        # Extração de dados
        self.button, self.values = window.Read()
    
    def Start(self):
        nome = self.values["nome"]
        email = self.values["email"]
        print(f"nome = {nome}")
        print(f"email = {email}")

tela = PythonScreen()
tela.Start()