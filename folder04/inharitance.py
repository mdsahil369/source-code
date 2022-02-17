class String:
    def __init__(self,string,string1):
        self.string = string
        self.string1 = string1
    
    def lenth(self):
        lenth = 0
        for i in self.string:
            lenth += 1
        return lenth 

class String1(String):
    def __init__(self, string,string1, number):
        super().__init__(string,string1)
        # String.__init__(self,string,string1)
        self.number = number

# s = String("Wikipedia is a free online encyclopedia.")
s = String1("Wikipedia is a free online encyclopedia.","jlfjljfl",7)

print(s.string1)

# print(s.string)
# print(s.lenth())



