
def constant_order1():   # O(1)
    start = 6
    end = 100
    mid = (end - start) // 2
    if mid % 2 == 0:
        del mid


def constant_order2():
    start = 7
    end = 0
    for i in range(1000):
        end += end * 2 + start


def linear1(n):     # O(n)
    sum = 0
    for i in range(n):
        # All below are O(1)
        x = 2 + 3 * 4
        sum += i
        sum += 2
        sum += x


def linear2(n):     # O(n)
    for i in range(10 * n):
        constant_order1()

    for i in range(5 * n):
        constant_order1()


def quadratic1(n):  # O(n^2)
    cnt = 0
    for i in range(5 * n):
        for j in range(3 * n):
            cnt += 1
            constant_order1()


def quadratic2(n):  # O(n^2)
    cnt = 0
    for i in range(5 * n):
        for j in range(3 * n):
            cnt += 1
            constant_order1()

    for i in range(10 * n):
        constant_order1()


def quadratic3(n):  # O(n^2)
    cnt = 0
    for i in range(5 * n):
        for j in range(3 * n):
            for k in range(1000):
                cnt += 1
                constant_order1()

    for i in range(10 * n):
        constant_order1()


def quadratic4(n):  # O(n^2)
    for i in range(10 * n):
        constant_order1()

    for i in range(3 * n * n):
        constant_order1()


def cubic1(n):  # O(n^3)
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                cnt += 1


def cubic2(n):  # O(n^3)
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                cnt += 1

    for i in range(1000 * n):
        for j in range(1000 * n):
            cnt += 1


def f(n):   # O(n^6)
    cnt = 0
    for i in range(n * n):
        for j in range(n):
            for k in range(n * n * n):
                cnt += 1


def f1(n):  # O(n^3)
    cnt = 0
    for i in range(n * n):
        for j in range(n):
            cnt += 1


def f2(n):  # O(n^4)
    for i in range(n):
        f1(i)


def f3(n, m):   # O(nm)
    cnt = 0
    for i in range(2 * n):
        for j in range(3 * m):
            cnt += 1


def f4(n, m):   # O(nm + n^3)
    cnt = 0
    for i in range(2 * n):
        for j in range(3 * m):
            cnt += 1

    for i in range(n * n * n):
        cnt += 1

