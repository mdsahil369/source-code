def sum(a,b):
    if type(a) == int and type(b) == int:
        return a+b
    else:
        raise ValueError("The data is worng !")
    
print(sum(2,'e'))