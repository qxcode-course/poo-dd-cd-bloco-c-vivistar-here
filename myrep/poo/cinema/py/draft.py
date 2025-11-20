class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone
    
    def getPhone(self) -> int:
        return self.phone
    
    def setPhone(self, phone: int):
        self.phone = phone

    def getId(self) -> str:
        return self.id
    
    def setId(self, id: str):
        self.id= id

    def __str__(self):
        return f"{self.id}:{self.phone}"
    
class Theater:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats: list[Client | None] = [None]

    def search(self, name: str):
        for i in range(len(self.seats)):
            client = self.seats[i]
            if client is not None and client.getId() == name:
                return i
            return None
        
    def verifyIndex(self, index: int) -> bool:
        return 0 <= index < len(self.seats)
    
    def reserve(self, id: str, phone: int, index: int) -> bool:
        if not self.verifyIndex(index):
            print("fail: cadeira nao existe")
            return False
        if self.seats[index] is not None:
            print("fail: cliente ja esta no sinema")

        self.seats [index] = Client(id, phone)
        return True
    
    def cancel(self, id: str):
        index = self.search(id)
        if index is None:
            print("fail: cliente nao esta no cinema")
            return 
        self.seats[index] = None

    def getSeats(self):
        return self.seats
    
    def __str__(self) -> str:
        lista: list[str] = []
        for client in self.seats:
            if client is None:
                lista.append("-")
            else:
                lista.append(str(client))
        mostrar = " ".join(lista)
        return "[" + mostrar + "]"
    
def main():
    theater = Theater(0)

    while True:
        line = input()
        args = line.split(" ")
        print("${line}")

        if args[0] == "end":
            break

        elif args[0] == "init":
            theater = Theater(int(args[1]))

        elif args[0] == "show":
            print(theater)

        elif args[0] == "reserve":
            theater.reserve(args[1], int(args[2]), int(args[3]))

        elif args[0] == "cancel":
            theater.cancel(args[1])

    main()
