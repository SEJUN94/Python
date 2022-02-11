class Animal:
    def __init__(self):
        self.mylife = 100
        self.myage = 0
    def getAge(self):
        self.myage += 1
        # self.mylife += -1
        self.mylife -= 1
    

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_lang = 1

    def exp(self,mama):
        self.skill_lang += mama

if __name__=='__main__':
    hum = Human()
    print(hum.mylife)
    print(hum.myage)
    print(hum.skill_lang)
    hum.getAge()
    hum.exp(100)
    print(hum.mylife)
    print(hum.myage)
    print(hum.skill_lang)
    

    