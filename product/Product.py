import csv

class Product:
    def Write(self,name, price, quantity, buy_price, sell_price, brand):
        with open('product/product.csv', 'w', newline='') as csvfile:
            fieldnames = ['name','price', 'quantity','buy_price','sell_price', 'brand']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'name': name, 'price': price, 'quantity' : quantity, 'buy_price' : buy_price, 'sell_price': sell_price, 'brand': brand})          

    def Read(self,csv):
        data_array = []
        print(type(csv))
        with open(csv, newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_array.append([row['name'], row['price'], row['quantity'], row['buy_price'], row['sell_price'], row['brand']])
            return data_array

