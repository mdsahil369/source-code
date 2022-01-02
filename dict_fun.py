# -----------------------Dictionary Methods-------------

# clear()	Removes all the elements from the dictionary

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()

# print(car)


# copy()	Returns a copy of the dictionary

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.copy()

# print(x)


# fromkeys()	Returns a dictionary with the specified keys and value

# x = ('key1','key2','key3')
# y = 1

# this_dict = dict.fromkeys(x,y)
# print(this_dict)



# get()	Returns the value of the specified key

# this_dict = {
#     'phone' : 'tesla',
#     'model' : 'Pi',
#     'year' : 2022
# }

# x = this_dict['model']
# print(x)




# items()	Returns a list containing a tuple for each key value pair

# this_dict = {
#     'phone' : 'tesla',
#     'model' : 'Pi',
#     'year' : 2022
# }
# x =  this_dict.items()
# print(x)






# keys()	Returns a list containing the dictionary's keys

# this_dict = {
#     'phone' : 'tesla',
#     'model' : 'Pi',
#     'year' : 2022
# }
# x =  this_dict.values()
# print(x)

# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair

# this_dict = {
#     'phone' : 'tesla',
#     'model' : 'Pi',
#     'year' : 2022
# }
# this_dict.popitem()
# print(this_dict)


# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# this_dict = {
#     'phone' : 'tesla',
#     'model' : 'Pi'
# }
# x =  this_dict.setdefault('year',2030)
# print(x)


# update()	Updates the dictionary with the specified key-value pairs

# this_dict = {
#     'phone' : 'tesla',
#     'model' : 'Pi'
# }
# this_dict.update({'year':2022,'version':1.0})
# print(this_dict)

# values()	Returns a list of all the values in the dictionary













