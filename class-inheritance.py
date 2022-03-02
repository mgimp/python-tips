# Inheritance
# You have two similar classes: Cat and Dog
""" class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark") """

# We can use inheritance to reduce the amount of code needed to create similar classes
# Both classes can inherit from an upper level Pet class
# We should only need to create the speak() method for each new class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    # Child methods with the same name override methods in the parent class
    def speak(self):
        print("I don't know what to say!")

class Cat(Pet): # Bracket entry inherits previous class
    def __init__(self, name, age, color):
        # Reference the super class (Pet)
        # '__init__' references the method we want to carry over
        # Saves us some recoding
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I am {self.color}.")

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()    # OUT: I am Tim and I am 19 years old
p.speak()   # OUT: I don't know what to say!

c = Cat("Bill", 34, "Orange")
c.show()    # OUT: I am Bill, I am 34 years old, and I am Orange.
c.speak()   # OUT: Meow

d = Dog("Jill", 25)
d.show()    # OUT: I am Jill and I am 25 years old
d.speak()   # OUT: Bark

f = Fish("Bubbles", 1)
f.show()
f.speak()