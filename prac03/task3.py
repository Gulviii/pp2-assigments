# 1. Қарапайым класс
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Aman")
p.greet()

# 2. Class vs instance variable
class Counter:
    count = 0   # class variable
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)  # 2

# 3. Object property өзгерту
p.age = 20
print(p.age)
del p.age  # property жою

# 4. Бірнеше объектілер
p2 = Person("Bob")
p2.greet()
