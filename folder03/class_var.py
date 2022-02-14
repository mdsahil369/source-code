class Car:
    offer = 12
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price

    def disc_price(self):
        # d = self.price - (self.price*Car.offer/100)
        d = self.price - (self.price*self.offer/100)
        return d

c = Car('Tesla Model X','Tesla',75000)
# Car.offer += 100
c.offer += 100
c1 = Car('Tesla Model S','Tesla',65000)

print(c.__dict__)
























# class Phone:
#     offer = 10
#     def __init__(self,name,brand,price):
#         self.name = name 
#         self.brand = brand
#         self.price = price

#     def disc_price(self):
#         p = self.price - int(self.price*self.offer/100)
#         return p

# phone1 = Phone('iPhone','Apple',120000)
# phone1.offer = 20
# print(phone1.disc_price())

