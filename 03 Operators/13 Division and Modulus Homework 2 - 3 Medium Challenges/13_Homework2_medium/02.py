
n = int(input())

# remember
# number % 10   => gets the last digit
# number // 10  => removes the last digit

# logic: get digit, remove it. Apply 3 times to get the last 3 digits

last1 = n % 10
n = n // 10

last2 = n % 10
n //= 10

last3 = n % 10
n //= 10

sum = last1 + last2 + last3
print(sum)
