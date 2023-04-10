total_cases = int(input())

pos = 0

while pos < total_cases:
    str = input()

    # In future we will learn about methods such as lower
    str = str.lower()
    # now str is lower case. There is only 2 cases for the code

    if str == "no" or str == "on":
        print('Match:', str)

    pos += 1

# The code only given for future reference. Skip if you can't get in 3 minutes
