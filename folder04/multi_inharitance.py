class String:
    def __init__(self,string):
        self.string = string
    
    def lenth(self):
        lenth = 0
        for i in self.string:
            lenth += 1
        return lenth 

class String1(String):
    def __init__(self, string, number):
        super().__init__(string)
        self.number = number
    def word(self):
        word = 0
        st = self.string.split(" ")
        for i in st:
            word += 1
        return word

class String2(String1):
    def __init__(self, string, number, boolean):
        super().__init__(string, number)
        self.boolean = boolean
    
    def upper(self):
        return self.string.upper()

s = String1("Wikipedia is a free online encyclopedia.",7)

print(s.string)
print(s.lenth())
print(s.word())
print(s.upper())




