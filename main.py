class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")

    def celebateBirthday(self):
        self.age += 1
        if (self.age != 1):
            print("Happy Birthday!" + " " + self.name +" is now " + str(self.age) + " years old!")
        else:
            print("Happy Birthday!" + " " + self.name +" is now " + str(self.age) + " year old!")
        
    def getInfo(self):
        print("Dog Name: " + self.name + ", Age: " + str(self.age))
    
doog1 = Dog("Doog", 3)

doog1.bark()
doog1.celebateBirthday()
doog1.getInfo()

    


