


# number = [1,2,3,4,5,6,7,8,9,10.9]


# print(any(type(i) == str for i in number))




def sum_of_all_numbers(*arge):
    sum = 0
    if all(type(i) == int or type(i) == float for i in arge):
        for i in arge:
            sum += i
        return sum
    else:
        return "Any Thinks Worng !"

print(sum_of_all_numbers(1,2,3,4))


