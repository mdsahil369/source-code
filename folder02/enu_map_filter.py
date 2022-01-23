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

name = ['1','2','3','4','5']
num = tuple(map(lambda a : int(a) ,name))


print(set(filter(lambda a : a > 2 , num)))


# print(name)




