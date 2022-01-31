# sorted()



# name = {'Sahil','Dot','Code','Apple'}

# var = set(sorted(name))

# print(var)

car = [
    {'Name':'Tesla','price':75190},
    {'Name':'BMW','price':120000},
    {'Name':'Lamborghini','price':500000},
]

var = sorted(car, key=lambda d : d['price'])
print(var)
























# car = [
#     {'Tesla':'Tesla','price':750000},
#     {'Apple':'Apple','price':8500000},
#     {'Lamborginy':'Lamborginy','price':950000},
# ]

# car0 = sorted(car, key=lambda d:d.get('price'))

# print(car0)