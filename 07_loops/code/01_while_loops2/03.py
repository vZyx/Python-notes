

while True:
    x, y = map(float, input().split())
    if y == 0:
        print("Y is zero!")
        break   # STOP the loop. Jump to line 10

    print(x / y)

print("Bye")

