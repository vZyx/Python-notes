

pos = 0
while pos < 5:
    print(pos, end=' ')
    pos += 1
print()

for pos in range(5):
    print(pos, end=' ') # 0 1 2 3 4
print()

for pos in range(2, 5):
    print(pos, end=' ') # 2 3 4
print()

rng = range(1, 21, 4)
for pos in rng:
    print(pos, end=' ') # 1 5 9 13 17
print()

