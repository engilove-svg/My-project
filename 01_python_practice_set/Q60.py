#create a class person with a constructor that accepts name and age as arguments and stores them as instant attributes, create an object and print the person's name and age
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)

p1=person("john",23)
p1.display()

    