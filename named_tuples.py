# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print(my_car.color)    # OUT: 'red'
print(my_car.mileage)  # OUT: 3812.4

# We get a nice string repr for free:
print(my_car)  # OUT: "Car(color='red' , mileage=3812.4)"

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'   # OUT: AttributeError: "can't set attribute"