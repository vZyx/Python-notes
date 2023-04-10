

def compute(numbers_lst, f1, f2):           # 9n+4
    for idx in range(len(numbers_lst)):     # 6n+1
        x = f1 - 1
        numbers_lst[idx] += x * (idx+1)

    sum = 0                         # 1
    for number in numbers_lst:      # 3n+1
        sum += number * f2

    return sum  # 1


print(compute([1, 2, 3, 4], 2, 4))


