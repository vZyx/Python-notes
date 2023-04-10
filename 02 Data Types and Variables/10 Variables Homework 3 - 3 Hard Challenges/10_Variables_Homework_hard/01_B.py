num1, num2, num3 = map(int, input().split())

# Pythonoic way
# # In the next section - assignment operator you should know why this works!
num1, num2, num3 = num2, num3, num1

print(num1, num2, num3)
