

count = 0
for a in range(1, 201):
    for b in range(1, 201):
        for c in range(1, 201):
            for d in range(1, 201):
                count += (a + b == c + d)

print(count)