
num = int(input())

is_even = num % 2 == 0

if is_even:
    print(num % 10)
else:
    if num < 1000:
        print(num % 100)
    elif num < 1000000:
        print(num % 10000)
    else:
        print(-num)
