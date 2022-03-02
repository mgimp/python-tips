# "magic" or "dunder" (double-under) methods are those that carry special significance in python classes and objects.

# __init__, __repr__, and __str__ are the most commonly used dunder methods.

# Other dunder methods exist such as int.__add__(x, y) and str.__add__('a', 'b') that can be modified in the class for our own purposes.

class Employee:

    # __init__ implicitly called at the starting script and defines attributes for the object instance.

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # __repr__ runs whenever we call repr(emp_1) on one of our objects.
    # Meant to be an unambiguous representation of the object for developers that aid in logging, debugging, etc.

    # If __repr__ exists but not __str__ exists, running str(emp_1) will call repr(emp_1) instead -- prioritize __repr__!

    def __repr__(self):

        # The objective is to return a string that we could use to recreate the object.

        # This is returned if you type in the instance name emp_1 outside of a print statement.
        
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # __str__ runs whenever we call str(emp_1) on one of our objects.

    # Readable representation of an object for use by the end user.

    def __str__(self):
        
        # Meant to be usable for an end user and is a little more flexible.

        # Printing the object print(emp_1) will call str(emp_1).     

        return '{} - {}'.format(self.fullname(), self.email)

    # We are replacing the existing __add__ dunder method with a special version for instances of this class.

    def __add__(self, other):

        # Return the sum of the current instance's pay attribute and another instance's pay attribute.

        return self.pay + other.pay

    # We are replacing the existing __len__ dunder method with the special version for instances of this class.

    def __len__(self):

        # Return the number of characters of the string returned by fullname().

        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2) # Takes advantage of our defined __add__ --> OUT: 110000

print(len(emp_1)) # Takes advantage of our defined __len__ --> OUT: 13