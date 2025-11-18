class Kid:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    def setAge(self, age: int):
        self.age = age

    def setName(self, name: str):
        self.name = name

    def toString(self):
        return f"{self.name}:{self.age}"
    
class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []

    def removeFromList(self, name: str, lista: list[Kid]) -> Kid | None:
        for i, kid in enumerate(lista):
           if kid.getName() == name:
               return lista.pop(i)
           return None
       
    
    def arrive(self, kid: Kid) -> None:
        self.waiting.insert(0, kid)

    def enter(self) -> None:
        if self.playing:
            kid = self.playing.pop(0)
            self.waiting.insert(0, kid)
        else:
            print("fail: nao ha crianças na fila de espera")

    def leave(self) -> None:
        if self.waiting:
            kid = self.waiting.pop(0)
            self.playing.insert(0, kid)
        else: 
            print("fail: nao ha crianças no pula pula")

    def removeKid(self, name: str) -> Kid | None:
        kid = self.removeFromList(name, self.playing)
        if kid:
            return kid
        return self.removeFromList(name, self.waiting)
    
    def toString(self) -> str:
        waiting_str = ", ".join(str(x) for x in reversed(self.waiting))
        playing_str = ", ".join(str(x) for x in self.playing)
        return f"[{waiting_str}] => [{playing_str}]"
        

def main():
    trampoline = Trampoline()

    while True:
        line = input()
        args = line.split(" ")
        print(f"${line}")

        if args[0] == "end":
            break

        elif args[0] == "arrive":
            name = args[1]
            age = int(args[2])
            kid = Kid(name, age)
            trampoline.arrive(kid)

        elif args[0] == "leave":
            trampoline.leave()

        elif args[0] == "show":
            print(trampoline.toString())

main()

