


num1, num2, num3 = map(float, input().split())

ans = num1

if ans > num2:
    ans = num2

if ans > num3:
    ans = num3

print(ans)

# This solution scales well
# If we have 10 numbers to get min
# we only add simple 10 if conditions

# scalability is an important industrial concept
# some website handles 10k users, another 10m, and third 2 billion

