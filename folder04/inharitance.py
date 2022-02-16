

# -------------------------- Laptop -------------------

class Laptop:
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
        self.alldata = f"This Laptop Name : {self.name} ,Brand : {self.brand} And Price : {self.price}"

laptop = Laptop('Dell XPS','Dell','1,27,000.00')


class Letest_Laptop(Laptop):
    def __init__(self,name,brand,price,ram,storage):
        Laptop.__init__(self,name,brand,price)
        self.ram = ram
        self.storage = storage

laptop0 = Laptop('Dell XPS','Dell','1,27,000.00')
laptop1 = Letest_Laptop('Dell XPS 2','Dell2','21,27,000.00','64 GB','1 TB')

print(laptop1.alldata)





