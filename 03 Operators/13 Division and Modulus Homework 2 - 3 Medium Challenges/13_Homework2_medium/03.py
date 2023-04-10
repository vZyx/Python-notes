
n = int(input())

# /1000 => removes last 3 digits

n_without_last_3_digits = n // 1000

# %10 get digit = 4th
print (n_without_last_3_digits % 10)