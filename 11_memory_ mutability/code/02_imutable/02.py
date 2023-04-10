

x = 'Hey'
y = x
z = 'Hey'

print(x is z)

print(id(x))        # 0x111
print(id(y))        # 0x111
print(id(z))        # 0x111
print(id('Hey'))    # 0x111

x += ' Most'
print(id(x))        # 0x222 ***
print(id(y))        # 0x111

x = 'Hey'
print(id(x))        # 0x111

#x[0] = 'R'         # TypeError