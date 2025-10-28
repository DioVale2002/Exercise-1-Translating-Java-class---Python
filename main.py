class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")

    def celebateBirthday(self):
        self.age += 1
        print("Happy birthday!" + " " + self.name +". You are now " + str(self.age) + " old!")

    def getInfo(self):
        print(self.name)
        print(str(self.age))
    
doog1 = Dog("Doog", 3)

doog1.bark()
doog1.celebateBirthday()
doog1.getInfo()

    


