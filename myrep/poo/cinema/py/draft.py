class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def getPhone(self) -> int:
        return self.phone

    def setPhone(self, fone: int):
        self.phone = fone
    
    def getId(self) -> str:
        return self.id
    
    def setId(self, id: str):
        self.id = id

    def toString(self) -> str:
        return f"{self.id}, {self.phone}"
    

class Theater:
    def __init__(self, capacity: int):        # construtor
        self.capacity = capacity
        self.seats: list[Client | None] = [None] * capacity

    def search(self, name: str):
        for i in range(len(self.seats)):    #vai acessar cada posição da lista usando i
            client = self.seats[i]          #pega o conteúdo da cadeira i e guarda no client
            if client is not None and client.getId() == name:      #ver se a cadeira tem um cliente e se o id é igual ao name
                return i                    #retorna o i
        return None
    
    def verifyIndex(self, index: int) -> bool:
        return 0 <= index < len(self.seats) #garante que o index tá entre 0 e o ultimo index válido (checagem)
    
    def reserve(self, id: str, phone: int, index: int) -> bool:
        if not self.verifyIndex(index):             #vê se a cadeira existe
            print("fail: cadeira nao existe")
            return False
        
        if self.seats[index] is not None:
            print("fail: cadeira ocupada")    #vê se a cadeira tá ocupada
            return False
        
        if self.search(id) is not None:
            print("fail: cliente ja esta na sala de cinema")   #vê se o cliente já está presente na sala
            return False
        
        self.seats[index] = Client(id, phone)  # faz a reserva
        return True
    
    def cancel(self, id: str):
        index = self.search(id)

        if index is None:
            print(f"fail: cliente {id} nao está na sala de cinema")
            return
        
        self.seats[index] = None

    def getSeats(self):
        self.seats: list[Client | None] 
        return self.seats
    
    def toString(self) -> str:
        lista: list[str] = []
        for client in self.seats:
            if client is None:
                lista.append("-")
            else:
                lista.append(str(client))

        mostrar = ", ".join(lista)
        return "[" + mostrar + "]"

def main():
    theater = Theater(0)

    while True: 
        line = input()
        args = line.split(" ")
        print(f"${line}")

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
        
