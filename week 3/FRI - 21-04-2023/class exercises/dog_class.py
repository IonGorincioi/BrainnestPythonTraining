# Create a Dog class with the following attributes:
# name, breed, and age. The class should also have
# the following methods: bark() and info().

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return "Woof, woof"

    def info(self):
        return f"{self.name} is {self.age} year's old and it's a {self.breed}"


dog = Dog("Stark", "bulldog", 5)
print(dog.info())
print(dog.bark())
