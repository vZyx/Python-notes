

num1, operation, num2 = input().split()
num1, num2 = float(num1), float(num2)

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
else:
    if num2 > 0:
        print(num1 / num2)
    else:
        print('NA')


