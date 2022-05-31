class BaseClass: pass
class SubClass(BaseClass): pass

print(issubclass(SubClass, BaseClass))
# OUT: True
print(issubclass(SubClass, object))
# OUT: True
print(issubclass(BaseClass, SubClass))
# OUT: False