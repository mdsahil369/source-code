# *args
# **kwargs

def full_name(**kwargs):
    for k,w in kwargs.items():
        print(f'{k} : {w}')
    # print(kwargs)

dict1 = {'first_name' : "Dot", "last_name" : "Code"}

full_name(**dict1)









