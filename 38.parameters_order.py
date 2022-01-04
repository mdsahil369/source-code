# *args
# **kwargs
# parameters
# default parameters

def function(first,*args,name = "default",**kwargs):
    print(first)
    print(args)
    print(name)
    print(kwargs)

function('code', 1,2,3,4 , f_name = "Dot" , l_name= "Code")







