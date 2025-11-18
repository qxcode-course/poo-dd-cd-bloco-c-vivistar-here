class Kid:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

    def toString(self):
        print(Kid)