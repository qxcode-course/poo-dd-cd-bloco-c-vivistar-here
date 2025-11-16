class Kid:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    def setAge(self, idade: int) -> None:
        if idade:
            self.age = idade
        else:
            print("fail: criança sem idade")
            
    def setName(self, nome: str) -> None:
        if nome:
            self.name = nome
        else:
            print("fail: criança sem nome")
        
    def toString(self) -> str:
        return f"{self.age}, {self.name}"
    
class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []

    def arrive(self, kid: Kid) -> None:
        self.kid.append(kid) #corrigir

    def enter(self) -> None:

    def leave(self) -> None:

    def removeKid(self, name: str) Kid | None:
