# object/instance mathod


class Number:
    def __init__(self,*args):
        self.args = args 

    def plas(self, h):
        n = 0
        for i in self.args:
            n += i
        return n + h


        # return self.num1 + self.num2
    # def square(self):
    #     return self.num1**self.num2

num = Number(2,3,3,4,5,66,4)

print(num.plas(10000))

list.append('jdfh')
