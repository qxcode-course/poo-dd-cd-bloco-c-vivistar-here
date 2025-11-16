class Kid:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    def setAge(self) -> None:
        if self.age is None: #olhar dps
            print("fail: criança sem idade")
            return
    
    def setName(self) -> None:
        if self.name is None:
            print("fail: criança sem nome")
            return
        
    def toString(self) -> str:
        return f"{self.age}, {self.name}"
    
