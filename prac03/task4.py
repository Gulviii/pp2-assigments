# 1. Parent және child class
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

d = Dog()
d.sound()

# 2. super() қолдану
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c = Car("Toyota", "Corolla")
print(c.brand, c.model)

# 3. Method overriding
class Bird(Animal):
    def sound(self):
        print("Chirp!")

b = Bird()
b.sound()

# 4. Multiple inheritance
class Flyer:
    def fly(self):
        print("Flying...")

class Eagle(Animal, Flyer):
    pass

e = Eagle()
e.sound()
e.fly()
