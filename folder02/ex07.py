
# name = ['x','y','z']
# age = [16,14,12]
# password = ['123','123','123']


var = (('x',16,'123'),('y',14,'123'),('z',12,'123'))


name,age,password = list(zip(*var))
print(list(name))
print(list(age))
print(list(password))

# print(dict(zip(name,age)))








# result =  []

# for i in range(len(name)):
#     result.append((name[i],age[i],password[i]))

# result = tuple(result)

# print(result)