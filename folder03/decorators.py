
from functools import wraps as w

def decorator_function(f):
    @w(f)
    def new_func(*args, **kwargs):
        """This is new function"""
        print("This is new function")
        return f(*args, **kwargs)
    return new_func

@decorator_function
def add(a,b):
    """This function add two number."""
    return a+b

print(add.__doc__)






# @func2
# def func1():
#     print("This is function 1")






























# def func2(f):
#     return f()   


# def decorator_func(func):
#     def new_func():
#         print("This is new function")
#         func()
#     return new_func

# @decorator_func
# def func1():
#     print("This is function 1")

# func1()




























# from functools import wraps

# def decorators_func(any_func):
#     @wraps(any_func)
#     def new_fuc(*args, **kwargs):
#         """This is new function"""
#         print('This is func')
#         return any_func(*args, **kwargs)
#     return new_fuc

# @decorators_func
# def func1(x,y):
#     """Tgx"""
#     return x+y

# print(func1.__doc__)

# def func2():
#     print('This is awsam function. 2')