### Single line if-statements
condition = True
x = 1 if condition else 0

### Underscores don't interrupt numbers
num1 = 10_000_000_000
num2 = 100_000_000
print(f'{(num1 + num2):,}') # OUT: 10,100,000,000

### Context Managers save us effort when messing with external data a lot
with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

### enumerate() function returns (array index, array contents) as a tuple
names = ['1', '2', '3']

for index, name in enumerate(names, start = 1):
    print(name)

### Looping over multiple lists at once using zip()
pets = ['lilly', 'cambie', 'omi']
cities = ['san francisco', 'chicago', 'boston']

for name, hero, city in zip(names, pets, cities):   # zip will stop after the shortest list is exhausted
    print(f'{name} is actually {hero} from {city}')

for value in zip(names, pets, cities):
    print(value)    # OUT: (1, lilly, san francisco)

### Unpacking tips
a, b = (1, 2)
print(a)
print(b)

a, b, _ = (1, 2, 3)   # You can use an underscore or leave the space blank if you don't want to use every value.
a, b, *c = (1, 2, 3, 4, 5)  # Asterisk will cause c to equal the rest of the values after 2
a, b, *_ = (1, 2, 3, 4, 5)  # Skip values after 2
a, b, *c, d = (1, 2, 3, 4, 5)  # c is equal to 3 & 4, d is equal to the last value

### Getting and setting attributes for an object
class Person():
    pass

person = Person()

### Adding an attribute
person.first = "Corey"
person.last = "Schafer"

# What happens when we want to set an attribute to a variable value?
first_key = "Joe"
first_val = "Ricci"

# person.first_key = first_val ----> This doesn't work because the attribute key would end up being named first_key

setattr(person, 'first', 'Joe')         # Method for adding keys, attributes
setattr(person, first_key, first_val)   # This works with variables

first = getattr(person, first_key)      # Returns attribute from a given key

person_info = {'first':'Corey', 'last':'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

### Password stuff (inputting sensitive information) / getpass()
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')    # In terminal, this will act like the 'sudo' password input

### Interactive python with the '-m' option
# '-m' will search sys.path for named module and execute contents as the __main__ module
# Allows you to execute scripts in other directories? And call code files without the .py extension?
# This is good when we're running files and don't want to change the sys.path?

### Learning about objects in python
# help(object_name)
# Displays useful information for the object

# dir(object_name)
# Displays valid attributes and methods for the object

# If you're working with a library and need help with a particular method, try opening shell and using the help() or dir() functions