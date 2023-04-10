

x = 30
y = x
z = 30

print(x is z)

print(id(x))    # 0x111
print(id(y))    # 0x111
print(id(z))    # 0x111
print(id(30))   # 0x111

x += 10
print(id(x))    # 0x222 ***
print(id(y))    # 0x111

x = 30
print(id(x))    # 0x111

