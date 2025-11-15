class Lead:
    def __init__(self, thickness: int, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self):
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        elif self.hardness == "6B":
            return 6
    

    def getSize(self):
        return self.size
    
    def getThickness(self):
        return self.thickness
    
    def getHardness(self):
        return self.hardness
    
    def setSize(self, size: int):
        self.size = size

    def toString(self) -> str:
        return f"{self.thickness}:{self.hardness}:{self.size}"

class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip: Lead | None = None
        self.barrel: list[Lead] = []

    def insert(self, lead: Lead) -> bool:
        if self.thickness != lead.getThickness():
            print("fail: gafrite não compatível")
            return False
        
        self.barrel.append(lead)
        return True
    
    def pull(self) -> bool:
        if self.tip is not None:
            print("fail: remova o grafite primeiro")
            return False
        
        if not self.barrel:
            print("fail: não tem grafite no tambor")
            return False
        
        lead = self.barrel.pop(0)
        self.tip = lead
        return True
    
    def remove(self) -> Lead | None:
        if self.tip is None:
            print("fail: não tem grafite no bico")
            return None
        
        lead = self.tip
        self.tip = None
        return lead
    
    def writePage(self) -> None:
        if self.tip is None:
            print("fail: não tem grafite no bico")
            return
        if self.tip.getSize() <= 10:
            print("fail: não é mais possível escrever com o grafite, por favor, retire o grafite")
            return
        
    def toString(self) -> str:
        return f"calibre: {self.thickness}, bico: {self.tip}, tambor: {self.barrel}"



def main():
    pencil = None

    while True:
        line = input()
        args = line.split(" ")
        print(f"${line}")

        if args[0] == "end":
            break

        elif args[0] == "init":
            thickness = float(args[1])
            pencil = Pencil(thickness)

        elif args[0] == "insert":
            pencil.insert

        elif args[0] == "pull":
            pencil.pull()

        elif args[0] == "remove":
            pencil.remove()
        
        elif args[0] == "write":
            pencil.writePage()

        elif args[0] == "show":
            print(pencil.toString())




main()