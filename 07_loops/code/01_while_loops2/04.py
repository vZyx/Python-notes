

while True:
    x, y = map(float, input().split())
    if y == 0:
        print("Y is zero!")
        continue   # jump to line 3

    print(x / y)

print("Bye")    # unreachable!

