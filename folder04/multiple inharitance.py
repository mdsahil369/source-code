class String:
    def __init__(self,name,age) -> None:
        pass
    def name(self):
        return "This class name is string"
class String1:
    def __init__(self) -> None:
        pass
    def name1(self):
        return "This class name is string1"

class String2(String,String1):
    def __init__(self) -> None:
        super().__init__()
    def name2(self):
        return "This class name is string2"


obj = String2()

print(obj.name())