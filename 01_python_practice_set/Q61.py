class animal:
    def sound(self):
        print("some sound")

class dog(animal):
    def sound(self):
        print("bark!")

p1=dog()
p1.sound()