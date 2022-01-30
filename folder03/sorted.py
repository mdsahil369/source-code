# sorted()

name = ('Sahil','Dot','Code')

def sorted(l):
    name = list(l)
    name.sort()
    name = tuple(name)
    return name


print(sorted(name))


























# name = ('Sahil','Dot','Code')

# def sorted(l):
#     l = list(l)
#     l.sort()
#     l = tuple(l)
#     return l

# print(sorted(name))






# car = [
#     {'Tesla':'Tesla','price':750000},
#     {'Apple':'Apple','price':8500000},
#     {'Lamborginy':'Lamborginy','price':950000},
# ]

# car0 = sorted(car, key=lambda d:d['price'])

# print(car0)