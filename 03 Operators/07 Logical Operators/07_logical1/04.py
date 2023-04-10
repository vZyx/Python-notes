

a, b, c, d = 10, 20, 30, 40

# a < b < c < d
# same as
# a < b and b < c and c < d
print(a < b < c < d)    # True
print(a < b < d > c)    # True
print(a < b < d < c)    # False

print(a == b == c == d) # False

