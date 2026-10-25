class animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Animal Name:", self.name)
class dog(animal):
    def sound(self):
        print("Dog Sound: Woof!")
d=dog("Buddy")
d.sound()
d.info()