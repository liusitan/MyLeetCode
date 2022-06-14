class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __hash__(self):
        return hash((self.age, self.name))
a = Person(0,"sitan")
b = Person(0,"sitan")
print(hash(a))
print(hash(b))
print(a==b)


# hash is different for different object, even with same class
class Person2:
    def __init__(self, age, name):
        self.age = age
        self.name = name
a = Person(0,"sitan")
b = Person(0,"sitan")
print(hash(a))
print(hash(b))
print(a==b)