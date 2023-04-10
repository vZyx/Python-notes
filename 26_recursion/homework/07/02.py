
def my_pow(value, p = 2):
    if p == 0:
        return 1

    return value * my_pow(value, p - 1) # 7^5 = 7 * 7^4


if __name__ == '__main__':
    print(my_pow(7))        # 49
    print(my_pow(7, 0))     # 1
    print(my_pow(7, 3))     # 343

