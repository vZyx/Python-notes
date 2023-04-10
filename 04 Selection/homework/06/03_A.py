
a, b, c = map(int, input().split())

# Assume numbers >= 0
res = -1
if res < a < 100:
    res = a

if res < b < 100:
    res = b

if res < c < 100:
    res = c

print(res)

# test: -10 -20 -30_oop