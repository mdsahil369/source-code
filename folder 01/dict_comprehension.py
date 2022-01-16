
# num = {i:i**2 for i in range(1,11)}
# print(num)


name = 'dot code'
# {'d' : 2 , 'o' : 2, 't' : 1}
string = {i:name.count(i) if name.count(i) < 2 else 1 for i in name}
print(string)
