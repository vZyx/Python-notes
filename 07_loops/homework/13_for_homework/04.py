
number = int(input())

if number <= 1:
    print("NO")
else:
    is_ok = True

    for i in range(2, number):
        if number % i == 0:
            is_ok = False
            break

    if is_ok:
        print("YES")
    else:
        print("NO")
