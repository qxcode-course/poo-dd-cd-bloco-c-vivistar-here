class Person:
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
        self.counters: list[Person | None] = [None] * counterCount
        self.queue: list[Person] = []

    def validateIndex(self, index: int) -> bool:
        return 0 <= index < len(self.counters)

    def toString(self) -> str:
        counters_str = ", ".join(
            map(lambda p: str(p.getNome()) if p is not None else "-----", self.counters)
            )
        queue_str = ", ".join(
            map(lambda p: str(p.getNome()) or "-----", self.queue))
        return f"Caixas: [{counters_str}]\nEspera: [{queue_str}]"
    

    def arrive(self, client: Person) -> None:
        self.queue.append(client)
        
    def call(self, index: int) -> None:
        if len(self.queue) == 0:
            print("fail: sem clientes")
            return
        if self.counters[index] is not None:
            print("fail: caixa ocupado")
            return
        self.counters[index] = self.queue.pop(0)   
        
    def finish(self, index: int) -> Person | None:
        if not self.validateIndex(index):
            print("fail: indice invalido")  #impedir que o usuário digita um número de caixa inexistente
            return  
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return None
        
        finished_client = self.counters[index]
        self.counters[index] = None
        return finished_client

    def cutInLine(self, sneaky: Person, gullible: str) -> bool:
        nomes_na_fila = [p.getNome() for p in self.queue]
        if sneaky.getNome() not in nomes_na_fila:
            print("fail: não fure fila")
            return False
        
        print(f"{sneaky.getNome()} está na posição correta.")
        return True

        
    def giveUp(self, quitter: str) -> bool:
        for person in self.queue:
            if person.getNome() == quitter:
                self.queue.remove(person)
                return True
            
        print("fail: pessoa desistiu de ficar na fila")
        return False

def main():
    Market = None

    while True:
        line = input()
        args = line.split(" ")
        print (f"${line}")

        if args[0] == "end":
            break

        elif args[0] == "init":
            caixas = int(parts[1]) #type: ignore
            market = Market(caixas) #type: ignore

        elif args[0] == "enter":
            if market is None:
                print("fail: mercado não inicializado")
                continue
            nome = parts[1]
            person = Person()
            person.setNome(nome)
            market.arrive(person)

        elif args[0] == "call":
            if marlet is None:
                print("fail: mercado não iniciado")
                continue
            index = int(parts[1])
            market.call(index)

        elif args[0] == "finish":
            if market is None:
                print("fail: mercado não iniciado")
                continue
            index = int(parts[1])
            market.finish(index)

        elif args[0] == "show":
            if market is not None:
                 print(market.toString()) #type: ignore
            else:
                print("fail: mercado não inicializado")

main()