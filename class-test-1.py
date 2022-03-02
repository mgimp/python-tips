# A Class creates an object type (like int, string, etc.)
# Classes are usually in CAML case

class Dog:

    # Instantiation (making an instance)
    # Is called whenever a Dog() instance is defined
    # Passes any arguments (arg) into Dog() as '__init__(arg)'
    def __init__(self, name_arg, age_arg):
        self.name = name_arg    # 'self.name' creates attribute of class 'Dog' which is called 'name' and equal to 'name_arg'
        self.age = age_arg
        print('%s is a good dog!' % self.name)  # Needs to be called as 'self.name' within a Dog method

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age_arg):
        self.age = age_arg

    # Methods are functions defined as part of an object that can be called on that object type
    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1

# Creating an object and playing with methods
d = Dog('Fido', 6)     # Assigns variable 'd' to Dog object type
print(d.name)       # OUT: Fido --> This prints the 'name' attribute
print(d.get_name())   # OUT: Fido
d.bark()            # OUT: bark
print(type(d))      # OUT: <class '__main__.Dog'>

# Creating an addition object
d2 = Dog('Bill', 2)    # 'Bill' is the value of the created 'name' attribute
print(d2.name)      # OUT: Bill --> This prints the 'name' attribute