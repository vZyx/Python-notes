# With mutable objects

# CPython 3.7 keeps some small integers in a common namespace
x, y = 30, 15 + 15
print(x is y)   # Probably True

x, y = x * 10000, y * 10000
print(x is y)   # Probably False

# same for strings: ASCII letters, digits, or underscores
x, y = 'hello', 'hello'
print(x is y)   # Probably True

x, y = x * 1000, y * 1000
print(x is y)   # Probably False

# ! not in the cashed list
x, y = 'hello!', 'hello!'
print(x is y)   # Probably False

z = x
print(x is z)   # Must be True

