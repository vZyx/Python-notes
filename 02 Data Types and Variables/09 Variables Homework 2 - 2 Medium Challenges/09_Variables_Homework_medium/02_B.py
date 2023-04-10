

num1, num2 = map(int, input().split())

# In the next section - assignment operator you should know why this works!
num1, num2 = num2, num1

print(num1, num2)
