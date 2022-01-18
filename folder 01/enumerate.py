from itertools import count

def ccc(a):
    return a


def counting(a):
    x = []
    for i in a:
        c = a.count(i)
        x.append(f'{i} = {c}')

    return x

# print(counting('dot code'))


