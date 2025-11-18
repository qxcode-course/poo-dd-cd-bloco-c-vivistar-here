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
        