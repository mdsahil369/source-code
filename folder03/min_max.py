
# num = (2,8,9,44,.6)



# name = ['Sahil','Dotte','Code']

# def func(i):
#     return len(i)

# print(max(name, key=lambda i : len(i)))





def max_str(l):
    """ This Function only work on list of strings ! """
    if all(type(a) == str for a in l):
        max_name = []
        num = []
        for i in l:
            num.append(len(i))

        for j in l:
            if len(j) == max(num):
                max_name.append(j)
        return max_name
    return "sorry"


name = ['Sahil','Dot',1,'code']
print(max_str(name))


help(len)

























# num = [9,4,12,8,6,5]

# print(max(num))

# ---------------------------------------------------------------

# def max_str(l):
#     """ This Function only work on list of strings ! """
#     if all(type(a) == str for a in l):
#         max_name = []
#         num = []
#         for i in l:
#             num.append(len(i))

#         for j in l:
#             if len(j) == max(num):
#                 max_name.append(j)
#         return max_name
#     return "sorry"


# name = ['Sahil','fffDot',1,'code']
# print(max_str(name))

# help(max_str)

# ------------------------------------------------------------------


# name = ['Sahil','Dotddm','Codjflkadjfe']


# print(max(name, key=lambda l:len(l)))




