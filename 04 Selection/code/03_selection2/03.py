

num = int(input())

if 100 <= num <= 200:
    print("Let's go deeper")

    if num % 2 == 0:
        print("ooh, even number")

        if num == 150:
            print('150 is lucky number!')

    else:
        print("Bye Mr Odd")
else:
    print("Have a good day")
