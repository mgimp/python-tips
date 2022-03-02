# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0
print(f"x={x}, y={y}, z={z}\n")

if x == 1 or y == 1 or z == 1:
    print('passed |==')
else: print('failed |==')

if x == 1 and y == 1 and z == 1:
    print('passed &==')
else: print('failed &==')

if 1 in (x, y, z):
    print('passed "in"')
else: print('failed "in"')

# Truthiness is general positivity or negation
# None ~ 0 ~ False
# [a-z] ~ >= 1 ~ True
# A variable having contents ~ True
# These only test for truthiness:
if x or y or z:
    print('passed "or"')
else: print('failed "or"')

if x and y and z:
    print('passed "and"')
else: print('failed "and"')

if any((x, y, z)):
    print('passed "any"')
else: print('failed "any"')

if all((x, y, z)):
    print('passed "all"')
else: print('failed" all"')