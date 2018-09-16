class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = int(age)
    def sit(self):
        print(self.name.title()+" is now siting")
    def age1(self):
        print(self.name.title()+" is "+ str(self.age) +" years old")
    def bark(self):
        name = self.name
        print(name +" is barking")
d = Dog("Tulla",26)
d.sit()
d.age1()
d.bark()
print(d.name)
print(d.age)