user = []

class Loging:
    def __init__(self,name,password):
        self.name = name
        self.password = password

class SignUp:
    def __init__(self,f_name,l_name,password,retype_password,number):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password
        self.retype_password = retype_password
        self.number = number
        user.append((self.f_name + self.l_name,self.password,self.number))

user_info = input('enter your first name, last name, password, retype password and number (seperat by , ) : ').split(',')


signup = SignUp(user_info[0],user_info[1],user_info[2],user_info[3],user_info[4])

user_loging = input('You Want to login (y/n): ')

if user_loging == 'y':
    user_log_info = input("right your blog : ")
    print(f"data: 1/0/3\n{user_log_info}\nThanks For Righting Your First Blog\n<b>{signup.f_name +' '+ signup.l_name}</b>")
    print(user)
