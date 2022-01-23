number = ['0','1','2','3','4','5']

num = tuple(map(int,number))
# num1 = tuple(filter(lambda a : a**2 ,num))


filt = list(filter(lambda a : a==5 , num))

print(filt)