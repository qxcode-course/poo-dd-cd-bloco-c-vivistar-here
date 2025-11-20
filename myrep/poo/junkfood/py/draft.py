#farei até 23h sena, tenho que dormir

class Slot:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name
    
    def getPrice(self, price: float):
        return self.price
    
    def getQuantity(self):
        return self.quantity
    
    def setName(self, name: str) -> None:
        self.name = name

    def setPrice(self, price: float):
        self.price = price

    def setQuantity(self, quantity: int):
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}:{self.price}:{self.quantity}"
    
class VendingMachine:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.slots: list[Slot]
        self.profit: float 
        self.cash: float
    
    def getSlot(self, index: int) -> Slot:
        return self.slots[index]
    
    def setSlot(self, index: int, slot: Slot) -> None:
        self.slots[index] = slot

    def clearSlot(self, index: int) -> None:

#n aguento mais q sono

    