

# Multiple assignments

x, y = 5, 7
print(x, y) # 5 7

a, b, c = 'hi', 12, 6.5
print(a, b, c)  # hi 12 6.5

x = y = z = 1
#x = y = z += 1     # invalid

m = 3
print(10 * m, m + 1)    # 30_oop 4
m, n = 10 * m, m + 1
print(m, n)             # 30_oop 4

# n is 4 NOT 31
# right-hand side is evaluated before the left-hand side.
# This is a source of error

# Avoid multiple assignments like this
# Use it for pure values and very simple and clear scenarios

c1, c2, c3 = 'Me!'
print(c1, c2, c3)   # M e !


