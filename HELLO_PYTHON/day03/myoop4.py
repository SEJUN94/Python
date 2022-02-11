from nbconvert.exporters.base import export
class Xi:
    def __init__(self):
        self.wealth = 10
    
    def myexport(self,quantity):
        self.wealth += quantity
        
    def myimport(self,quantity):
        self.wealth -= quantity
        
    def hanhanryong(self):
        print("못가져가")
    
class Baiden:
    def __init__(self):
        self.military_power = 10
        
    def makePower(self):
        self.military_power += 1
        
class TaeHyung(Xi,Baiden):
    def __init__(self):
        Xi.__init__(self)
        Baiden.__init__(self)
        
        
if __name__=='__main__':
    th = TaeHyung()
    print(th.wealth)
    print(th.military_power)
    th.myexport(1)
    th.makePower()
    print(th.wealth)
    print(th.military_power)
    
    
        