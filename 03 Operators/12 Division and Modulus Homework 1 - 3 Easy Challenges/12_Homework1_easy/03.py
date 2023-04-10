

n, m = map(int, input().split())

# let's try 13/5
# 13/5 = 2  [2 complete units, each is 5]
# 2*5 = 10  [total complete units]
# Reminder is 13-10 = 3. This number generates the fractional part
result = n - (n // m) * m

print(result)

