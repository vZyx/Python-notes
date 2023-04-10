
test_cases = int(input())

for case in range(test_cases):
    n, sum = int(input()), 0
    for pos in range(1, n+1):
        sum += pos

    print('Sum from 1 to ', n, '=', sum)
