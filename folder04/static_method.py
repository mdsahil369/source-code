class Car:
    offer = 12
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    
    @staticmethod
    def help():
        return "This Class Name is Car"

    @classmethod
    def Dis(cls,name,brand,price):
        n = name
        b = brand
        p = price
        return f"You offer is {cls.offer}% Name = {n} Brand = {b} Price = {p}"

    def disc_price(self):
        # d = self.price - (self.price*Car.offer/100)
        d = self.price - (self.price*self.offer/100)
        return d



print(Car.help())








# c = Car('Tesla Model X','Tesla',75000)

# print(Car.Dis('Tesla Model X','Tesla',75000))
# print(c.disc_price())






# Car.offer += 100
# c.offer += 100
# c1 = Car('Tesla Model S','Tesla',65000)

# print(c.disc_price())



