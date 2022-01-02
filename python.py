
#    -------------------Exercise------------------  

# 1. Enter your G-mail : 
# 2. split()
# 3. gmail --> yahoo
# 4. Your New email is : .....@yahoo.com

# Ex:
# Enter your G-mail : william369@gmail.com
# Your New email is : william369@yahoo.com

# Challenge
# replace() function [Help by Google]

# email_f, email_l = input("Enter Your G-mail : ").split("@")
# email = email_f + "@yahoo.com"
# print("Your New Email Is : " + email) 

# email = input("Enter Your G-mail : ")
# new_email = email.replace("gmail","yahoo")
# print("Your New Email Is : " + new_email) 




















# email_f,email_l = input("Enter your G-mail : ").split("@")
# email = email_f + "@yahoo.com"
# print("Your New email is :" + email)

# email_f = input("Enter your G-mail : ")
# email = email_f.replace("gmail","yahoo")
# print("Your New email is :" + email)








# import turtle

# colors=["red","purple","blue","green","orange","yellow"]
# t=turtle.Pen()
# turtle.bgcolor("black")
# t.speed(0)
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x//100+1)
#     t.forward(x)
#     t.left(59)





# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pensize(2)
# t.speed(30)
# for i in range(18):
#     for col in ("red","purple","blue","green","orange","yellow"):
#         t.color(col)
#         t.circle(90)
#         t.left(10)
# t.hideturtle()














name = "python"
p = name[-1::-2]
print(p)



























