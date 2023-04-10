
# You can use () to force priority
age, salary = 30, 7000

result = (age > 25) and (salary < 8000) # True

# but > is higher in precedence than and, so parentheses can be removed

result = age > 25 and salary < 8000 # True
print(result)

print(age > 25 and salary > 9000)   # False

print(age > 35 or salary < 8000)   # True

print(age > 35 or salary > 9000)   # False

