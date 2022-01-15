# list comprehension 



# num = [i**2 for i in range(1,11)]

# for i in range(1,11):
#     num.append(i**2)

# print(num)




# u_foods = []
foods = ['apple','banana','kiwi']
u_foods = [i.upper() if 'a' in i else i for i in foods]

# for i in foods:
#     if 'a' in i:
#         u_foods.append(i.upper())
#     else:
#         u_foods.append(i)


print(u_foods)



































# num = []

# for i in range(1,11):



#     num.append(i**2)

# print(num)

# num1 = [i**2 for i in range(1,11)]
# print(num1)

# foods = ['apple','banana','cherry','kiwi','mango']

# foods_one = [i if 'a' in i else 'b' if 'b' not in i else 'c' for i in foods ]
# print(foods_one)