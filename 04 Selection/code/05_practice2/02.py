

n = int(input())

if n < 10000:
    print("This is a small number")
else:
    digit1 = n%10
    n = n//10
    digit2 = n%10
    n = n//10
    digit3 = n%10      # old value of n lost

    sum = digit1 + digit2 + digit3

    if sum%2 != 0:   # odd
        print("This is a great number")
    else:
        is_digit1_odd = digit1 % 2 != 0
        is_digit2_odd = digit2 % 2 != 0
        is_digit3_odd = digit3 % 2 != 0

        if is_digit1_odd or is_digit2_odd or is_digit3_odd:
            print("This is a good number")
        else:
            print("This is a bad number")

