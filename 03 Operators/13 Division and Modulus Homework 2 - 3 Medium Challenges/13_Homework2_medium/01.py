num = int(input())


# Is even using %2
is_even1 = num % 2 == 0

# is even using /2
by2 = num / 2.0         # this is either X.0 or X.5  try 10, 11
by2 = by2 - num//2    # Remove X. This is now either 0 for even or 0.5 for odd
is_even2 = by2 == 0

# is even using %10
last_digit = num % 10	    # even last digit is 0, 2, 4, 6, 8
is_even3 = last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

print(is_even1, is_even2, is_even3)

# If using both / and //
is_even4 = num / 2 == num // 2
print(is_even4)
