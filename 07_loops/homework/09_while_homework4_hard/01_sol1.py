total_cases = int(input())

pos = 0

while pos < total_cases:
    str = input()

    # there are 8 different ways to make 2 letters no in lower/upper cases
    if str == "no" or str == "No" or str == "nO" or str == "NO" or \
        str == "on" or str == "oN" or str == "On" or str == "ON":
        print('Match:', str)

    pos += 1

# Observe \ in end of line 9
# It allows us to split a long exprssion on several lines