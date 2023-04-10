def f1(n=1000):     # O(n^3
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                cnt += 1
    # cnt = 1000,000,000


def f2(n=1000):     # O(n^3
    cnt = 0
    for i in range(n):
        for j in range(i, n, 1):
            for k in range(j, n, 1):
                cnt += 1

    return cnt
    # cnt 167,167000


print(f2())


