# polymorphism
# spatial/magic/dunder methods


# string = 10
# print(type(string.__str__()))

# print(dir(int))






# list()
# num = {1,2,3,4,5}

# change = list(num)

# print(type(change))





class Person:
    def __init__(self,f_name,l_name,password):
        self.f_name = f_name
        self.l_name = l_name
        self._password = password
    
    def __name__(self):
        return f"User Name : {self.f_name} {self.l_name}"

    def __str__(self):
        return f"({self.f_name},{self.l_name},{self._password})"
    def __repr__(self):
        return f"(Person('{self.f_name}','{self.l_name}','{self._password}'))"

obj = Person('All','Subscriber','all')
obj1 = Person('All','Subscriber','all')
print(obj1.__repr__())


# obj = list([1,2,3])
# print(obj)




























# print(dir(int))

# num = 10
# print(num + 5)
# print(num.__add__(5))

# string = 1234567
# print(type(string.__str__()))

# string = "1234567"
# print(string.__len__())

# flo = 12.7
# print(flo.__round__())

# name = "Dot Code"
# print(name.replace('D','I'))


# class Person:
#     def __init__(self,f_name,l_name,password):
#         self.f_name = f_name
#         self.l_name = l_name
#         self._password = password
    
#     def __name__(self):
#         return f"User Name : {self.f_name} {self.l_name}"

#     def __str__(self):
#         return f"(__str__.{self.f_name},{self.l_name},{self._password})"
#     def __repr__(self):
#         return f"(__repr__.{self.f_name},{self.l_name},{self._password})"

# obj = Person('All','Subscriber','all')
# print(obj)


