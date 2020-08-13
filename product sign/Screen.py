import PySimpleGUI as sg
import tkinter
from Product import Product

class Screen:
    def __init__(self):
        layout = [
            [sg.Text("Produto"), sg.Input(size=(50,10),key="name")],
            [sg.Text("Preço"), sg.Input(size=(50,10),key="price")],
            [sg.Text("quantidade"), sg.Input(size=(50,10),key="quantity")],
            [sg.Text("Preço de Compra"), sg.Input(size=(50,10),key="buy_price")],
            [sg.Text("Preço de Venda"), sg.Input(size=(50,10),key="sell_price")],
            [sg.Text("Marca"), sg.Input(size=(50,10),key="brand")],
            [sg.Button("Cadastrar"), sg.Cancel()]
        ]

        window = sg.Window("Cadastro de produtos", layout)

        self.button, self.values = window.Read()

    def Start(self):
        name = self.values["name"]
        price = self.values["price"]
        quantity =  self.values["quantity"]
        buy_price = self.values["buy_price"]
        sell_price = self.values["sell_price"]
        brand = self.values["brand"]
        
        product = Product()
        product.Write(name, price, quantity, buy_price, sell_price, brand)