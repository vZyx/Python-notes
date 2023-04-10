N = int(input())

number = 0

while N > 0:
    last_digits = N % 10
    N //= 10    # remove last digit

    number = number * 10 + last_digits

print(number, number * 3)

# In the future we will learn how to do that without the above math
# E.g.
N = 1234
str_num = str(N)        # convert to string
str_num = str_num[::-1] # reverse string
N = int(str_num)
print(N, N*3)
