
num = int(input())

digits = 0

while num > 0:
    digits += 1
    num //= 10

print('# of digits of', num, 'is', digits)

# There are 3 BUGS in this code
# Find a test-case per mistake!