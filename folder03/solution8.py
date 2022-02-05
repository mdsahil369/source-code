

# Class --> Phone --> name,brand,price,size,camera

class Phone:
    def __init__(self,name,brand,price,size,camera):
        self.name = name
        self.brand = brand
        self.price = price
        self.size = size
        self.camera = camera

p = Phone('infinix hot 10 play','infinix',10000,7.5,'15 mpx')
print(f"name = {p.name}")
print(f"brand = {p.brand}")
print(f"price = {p.price}")
print(f"size = {p.size}")
print(f"camera = {p.camera}")