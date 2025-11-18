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
        if not self.waiting:
            return
        kid = self.waiting.pop()
        self.playing.insert(0, kid)
    
    def leave(self) -> None:
        if not self.playing:
            return
        kid = self.playing.pop()
        self.waiting.append(kid)


    def removeKid(self, name: str) -> Kid | None:
        kid = self.removeFromList(name, self.waiting)
        if kid:
            return kid
        kid = self.removeFromList(name, self.playing)
        if kid:
            return kid
        print(f"fail: {name} nao esta no pula-pula")
        return None
    
    def toString(self) -> str:
        waiting_str = ", ".join(x.toString() for x in (self.waiting))
        playing_str = ", ".join(x.toString() for x in self.playing)
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

        elif args[0] == "enter":
            trampoline.enter()

        elif args[0] == "leave":
            trampoline.leave()

        elif args[0] == "remove":
            name = args[1]
            trampoline.removeKid(name)

        elif args[0] == "show":
            print(trampoline.toString())

main()


# sabado eu me mato
# eeeee
# sabado eu me mato, oba!
# sabado eu me mato