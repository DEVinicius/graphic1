import PySimpleGUI as sg
import tkinter
from Product import Product

class Screen:
    def MainPage(self):
        layout = [
            [sg.Text("Produto"), sg.Input(size=(50,10),key="name")],
            [sg.Text("Preço"), sg.Input(size=(50,10),key="price")],
            [sg.Text("quantidade"), sg.Input(size=(50,10),key="quantity")],
            [sg.Text("Preço de Compra"), sg.Input(size=(50,10),key="buy_price")],
            [sg.Text("Preço de Venda"), sg.Input(size=(50,10),key="sell_price")],
            [sg.Text("Marca"), sg.Input(size=(50,10),key="brand")],
            [sg.Button("Cadastrar")]
        ]

        window = sg.Window("Cadastro de produtos", layout)

        self.button, self.values = window.Read()
        window.Close()

    def Start(self):
        self.MainPage()
        print(self.button)
        product = Product()
        if self.button == 'Cadastrar':
            name = self.values["name"]
            price = self.values["price"]
            quantity =  self.values["quantity"]
            buy_price = self.values["buy_price"]
            sell_price = self.values["sell_price"]
            brand = self.values["brand"]
            
            product.Write(name, price, quantity, buy_price, sell_price, brand)
            self.MainPage()
        else:
            exit()