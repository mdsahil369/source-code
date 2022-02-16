# -------------------------- Laptop -------------------

class Laptop:
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
        # self.alldata = f"This Laptop Name : {self.name} ,Brand : {self.brand} And Price : {self.price}"
    @property
    def alldata(self):
        return f"This Laptop Name : {self.name} ,Brand : {self.brand} And Price : {self.price}"
    @alldata.setter
    def alldata(self,new_price):
        self.price = new_price

laptop = Laptop('Dell XPS','Dell','1,27,000.00')

laptop.price = 100000

print(laptop.price)

laptop.alldata = f"This Laptop Name : {laptop.name} ,Brand : {laptop.brand} And Price : {laptop.price}" + " , ram 16 GB"

print(laptop.alldata)


