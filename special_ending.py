#!/usr/bin/env python3

# Using script from magic_dunder_methods.py

import time

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

def main():
    print(emp_1)
    time.sleep(1.5)
    print(emp_2)
    time.sleep(1.5)
    print(emp_1 + emp_2)
    time.sleep(1.5)


if __name__ == '__main__':
    try:
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Test', 'Employee', 60000)
        main()
        ## your code, typically one function call
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print("Press Enter to continue ...")
        input()