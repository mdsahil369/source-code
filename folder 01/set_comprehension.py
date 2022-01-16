# list comprehension 



# num = [i**2 for i in range(1,11)]

# for i in range(1,11):
#     num.append(i**2)

# print(num)



# foods = ['apple','banana','kiwi']

# u_foods = {first[0] for first in foods}
# print(u_foods)

num = {s**2 for s in range(1,11) if s < 5}
print(num)


































# num = []

# for i in range(1,11):



#     num.append(i**2)

# print(num)

# num1 = [i**2 for i in range(1,11)]
# print(num1)

# foods = ['apple','banana','cherry','kiwi','mango']

# foods_one = [i if 'a' in i else 'b' if 'b' not in i else 'c' for i in foods ]
# print(foods_one)