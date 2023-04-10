
num = int(input())
num2 = num  # copy

digits = 0

while num > 0:
    digits += 1
    num //= 10

print('# of digits of', num2, 'is', digits)

# There are 2 BUGS in this code

