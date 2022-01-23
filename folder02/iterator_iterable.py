# enumerate


# name = [1,2,3,4,5]

# for pos,i in enumerate(name):
#     print(f'{pos} = {i}')



# map

# name = ['1','2','3','4','5']

# # def num(a):
# #     return int(a)

# print(tuple(map(lambda a : int(a) ,name)))

# print(name)




# filter

name = ['1','2','3','4','5']  #---> itarables
num = map(lambda a : int(a) ,name) #-- > itarator

# print(name)
# print(num)

var = iter(name)
print(next(var))
print(next(var))
print(next(var))

# for i in num:
#     print(i)






