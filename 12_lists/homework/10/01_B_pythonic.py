def is_increasing(lst):
    # let's make it more pythonic
    # we create a list that allows us to compare element by element

    last_item = lst[len(lst) - 1]
    shifted_lst = lst.copy()
    shifted_lst.pop(0)  # we don't compare first with previous
    shifted_lst.append(last_item)

    # for input      [10 20 30_oop 40]
    # shifted_lst is [20 30_oop 40 40]

    print(lst)
    print(shifted_lst)

    # You will learn this style soon. Lecture video is not fully correct
    return all(lst[idx] <= shifted_lst[idx] for idx in range(len(lst)))


def is_increasing_v2(lst):
    # We can write above logic in a single line too.
    # But you did not learn zip yet

    return all(x < y for x, y in zip(lst, lst[1:]))



if __name__ == '__main__':
    lst = list(map(int, input().split()))

    status = is_increasing(lst)
    print(status)

    if status:
        print('YES')
    else:
        print('NO')
