# -------------------------------Exercise------------------------------------
# task 01
# thislist = ['name','email','password','phone']
# thistuple = ('dot_code','dotcode@gmail.com','xxxxxxx','xxxxxxxxxxx')

# for / while

# thisdict ={'name': 'dot_code', 'email': 'dotcode@gmail.com', 'password': 'xxxxxxx', 'phone': 'xxxxxxxxxxx'}

# task 02
# thisdict ={'name': 'dot_code', 'email': 'dotcode@gmail.com', 'password': 'xxxxxxx', 'phone': 'xxxxxxxxxxx'}

# thislist = ['name','email','password','phone']
# thistuple = ('dot_code','dotcode@gmail.com','xxxxxxx','xxxxxxxxxxx')






# task 01
# thislist = ['name','email','password','phone']
# thistuple = ('dot_code','dotcode@gmail.com','xxxxxxx','xxxxxxxxxxx')

# thisdict = {}

# if len(thislist) == len(thistuple):
#     for i in range(len(thislist)):
#         thisdict.update({thislist[i]:thistuple[i]})
#     print(thisdict)
# else:
#     print('The lenth of list is not equall to tuple .')



# for / while

# thisdict ={'name': 'dot_code', 'email': 'dotcode@gmail.com', 'password': 'xxxxxxx', 'phone': 'xxxxxxxxxxx'}





# task 02
thisdict ={'name': 'dot_code', 'email': 'dotcode@gmail.com', 'password': 'xxxxxxx', 'phone': 'xxxxxxxxxxx'}

thislist = []
thistuple = ()
ct = list(thistuple)

for x,y in thisdict.items():
    thislist.append(x)
    ct.append(y)

thistuple = tuple(ct)

print(thislist)
print(thistuple)


# thislist = ['name','email','password','phone']
# thistuple = ('dot_code','dotcode@gmail.com','xxxxxxx','xxxxxxxxxxx')

