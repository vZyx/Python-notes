

n = int(input())

row = n
while row > 0:
    stars_count = 1

    while stars_count <= row:
        print('*', end='')
        stars_count += 1

    print()
    row -= 1

