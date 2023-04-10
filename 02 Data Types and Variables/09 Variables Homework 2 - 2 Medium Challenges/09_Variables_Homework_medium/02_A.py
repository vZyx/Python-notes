

num1, num2 = map(int, input().split())

# create temporary to hold num1
num3 = num1
# give num1 value of num 2
num1 = num2
# now give num2 the temp value
num2 = num3

print(num1, num2)




# Note: this is more like a C++/Java thinking
