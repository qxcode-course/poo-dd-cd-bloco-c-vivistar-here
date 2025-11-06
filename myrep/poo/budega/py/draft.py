class Client:
    def __init__(self):
        self.__nome: str | None = None

    def getNome(self) -> str | None:
        return self.__nome
    
    def setNome(self, valor: str) -> None:
        if valor: 
            self.__nome = valor
        else:
            print("fail: comando inválido")

    def toString(self):
        return f"{self.__nome}"
    
    def __str__(self):
        if self.__nome is None:
            return "Pessoa sem nome"
        return f"Nome: {self.__nome}"



class Market:
    def __init__(self, counterCount: int):
        self.counters: list[Client | None] = [None] * counterCount
        self.queue: list[Client] = []

    def validateIndex(self, index: int):
    
    def Market(self, countCounter: int):

    def toString(self):
        return f"{self.counters}"

    def arrive(client: Client)
        
    def call()
        
    def finish()
        
    def cutInLine()
        
    def giveUp()