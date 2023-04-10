
n = int(input())

is_even = n % 2 == 0
is_odd = not is_even

# formula of 2 parts: only one of them will be activated
result = is_even * 100 + is_odd * 7

# In the future, with if condition, you don't need to think in a formula

print(result)