# Class attributes are those specific to the class, not to an instance (object of that class)
# Class methods are accessible only though the class and not through the instance

from os import stat


class Person:
    # Attribute not specific to any instance - It will be consistant through all instances
    # All child references to this attribute will return the current value
    number_of_people = 0    

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # This method is not specific (doesn't have access to) to any one instance
    # That's why there is no 'self' attributes
    # This is supposed to be called on the class itself
    @classmethod    # This is a decorator
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")

print(p1.number_of_people)  # OUT: 2
print(p2.number_of_people)  # OUT: 2
Person.number_of_people = 8
print(p1.number_of_people)  # OUT: 8

print(Person.number_of_people_())   # OUT: 8




# Static methods do stuff but don't change anything
# This is most useful for organization

# I want to be able to call methods from this class at any point regardless of/without an instance
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("RUN")

print(Math.add5(5)) # OUT: 10
print(Math.add10(5)) # OUT: 15
Math.pr()