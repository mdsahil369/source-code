def num_join(*args):
    num = 0
    for i in args:
        num += i
    return num

tuple1 = (5,7,8)

print(num_join(*tuple1))

