class Pencil:
    def __init__(self, thickness: int, barrel:str):
        self.thickness = thickness
        self.tip = Lead | None =None
        self.barrel = barrel    

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
    