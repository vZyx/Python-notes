
num = int(input())
num2 = num  # copy

if num == 0:
    digits = 1
else:
    digits = 0
    while num > 0:
        digits += 1
        num //= 10

print('# of digits of', num2, 'is', digits)

# There is 1 BUG in this code

