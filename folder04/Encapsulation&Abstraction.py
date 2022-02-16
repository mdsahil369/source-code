class String:
    def __init__(self,string):
        self.__string = string
    
    def lenth(self):
        lenth = 0
        for i in self.string:
            lenth += 1
        return lenth
    def word(self):
        word = 0
        st = self.string.split(" ")
        for i in st:
            word += 1
        return word

s = String("Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation jksfj.")


print(s._String__string)


# print(s.lenth())
# print(s.word())

# len()










































# -------------------------- Laptop -------------------

# class Laptop:
#     def __init__(self,name,brand,price):
#         self.name = name
#         self.brand = brand
#         self.price = price
#     def allData(self):
#         return f"This Laptop Name : {self.name} ,Brand : {self.brand} And Price : {self.price}"
#     def 

# laptop = Laptop('Dell XPS','Dell','1,27,000.00')

# print(laptop.allData())







































# class Laptop:
#     def __init__(self,name,brand,price):
#         self.name = name
#         self.brand = brand
#         self.price = price
#         # self.alldata = f"This Laptop Name : {self.name} ,Brand : {self.brand} And Price : {self.price}"
    
#     @property
#     def alldata(self):
#         return f"This Laptop Name : {self.name} ,Brand : {self.brand} And Price : {self.price}"
#     @alldata.setter
#     def alldata(self,new_price):
#         self.price = new_price

# laptop = Laptop('Dell XPS','Dell','2,75,000.00')

# laptop.price = 300000.0 
# # laptop.alldata = f"This Laptop Name : {laptop.name} ,Brand : {laptop.brand} And Price : {laptop.price}"
# # print(laptop.price)

# laptop.alldata = laptop.alldata + " , ram 16GB"

# # kdfjakjflkaj
# # kfljlkfjlafj
# laptop.alldata = laptop.alldata + " , storage 1TB"

# print(laptop.alldata)









