

# is  : check if SAME memory/reference
# ==  : check if equal value!


x, y = 123456789, 123456789

print(x == y)   # True
print(x is y)   # Probably False

# but remember small values with is
x, y = 10, 10
print(x is y)   # Probably True

# as implementation dependent
# be careful from is operator
# use it to check types

