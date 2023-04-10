
# priority: not, and, or
age, salary, weight = 30, 7000, 110

print(age > 25 and salary < 8000 and weight < 150)  # True
print(age > 25 and salary < 8000 and weight > 200)  # False
print(age > 35 or salary > 6000 or weight > 200)    # True
print(age > 35 and salary > 6000 or weight > 200)   # False
print(age > 20 and salary > 6000 or weight > 200)   # True

status = weight >= 150
print(age > 25 and salary < 8000 and not status)    # True

