

num1, num2, num3 = map(int, input().split())

# one way to swap num1, num2 in 3 lines
# then swap swap num2, num3 in 3 lines

# a smarter idea to circulate them (like a circle)

temp = num1
num1 = num2
num2 = num3
num3 = temp

print(num1, num2, num3)
