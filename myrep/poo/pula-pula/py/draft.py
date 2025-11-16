class Kid:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    def setAge(self, idade: int) -> None:
        if idade is not None:
            self.age = idade
        else:
            print("fail: criança sem idade")
            
    def setName(self, nome: str) -> None:
        if nome:
            self.name = nome
        else:
            print("fail: criança sem nome")
        
    def toString(self) -> str:
        return f"{self.age}:{self.name}"
    
class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []

    def arrive(self, kid: Kid) -> None:
        self.waiting.append(kid) 

    def enter(self) -> None:
        if self.waiting:
            kid = self.waiting.pop(0)
            self.playing.append(kid)
        else:
            print("fail: nao ha crianças na fila de espera")

    def leave(self) -> None:
        if self.playing:
            kid = self.playing.pop(0)
            self.waiting.append(kid)

    def removeFromList(self, name: str, lista: list[Kid]) -> Kid | None:
        for kid in lista:
            if kid.getName() == name:
                lista.remove(kid)
                return kid
        return None

    def removeKid(self, name: str) -> Kid | None:
        kid = self.removeFromList(name, self.playing)
        if kid:
            return kid
        return self.removeFromList(name, self.waiting)
    
    def toString(self) -> str:
        waiting_str = ",".join([f"{kid.getName()}:{kid.getAge()}" for kid in reversed(self.waiting)])
        playing_str = ",".join([f"{kid.getName()}:{kid.getAge()}" for kid in self.playing])
        return f"[{playing_str}] => [{waiting_str}]"


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
            idade = int(args[2])
            kid = Kid(idade, name)
            trampoline.arrive(kid)

        elif args[0] == "leave":
            trampoline.leave()

        elif args[0] == "show":
            print(trampoline.toString())
main()