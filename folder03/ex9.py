

# EXERCISE:
#    StringInfo
#    words()
#    character()

#    without len() function 
#    with lenth() function



def lenth(obj):
    lenth = 0
    for i in obj:
        lenth += 1
    return lenth


class StringInfo:
    def __init__(self,string):
        self.string = string

    def character(self):
        return lenth(self.string)
    def words(self):
        return lenth(self.string.split(" "))
    def upper(self):
        return self.string.upper()
    def lower(self):
        return self.string.lower()

s = StringInfo('My Name Is Sahil ljf kfljlfdkj k f ljf')
print(s.lower())





