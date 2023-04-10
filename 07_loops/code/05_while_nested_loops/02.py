

n = int(input())

row = 1
while row <= n:
    stars_count = 1

    while stars_count <= row:
        print('*', end='')
        stars_count += 1

    print()
    row += 1

