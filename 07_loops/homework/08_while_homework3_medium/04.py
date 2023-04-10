total_cases = int(input())

# Outer loop for cases
while total_cases > 0:
    numbers_cnt = int(input())

    pos = 0
    result = 0

    # Inner loop to read a case
    while pos < numbers_cnt:
        value = int(input())

        if pos == 0:
            result = value
        elif result > value:
            result = value

        pos += 1

    print('Min value is:', result)
    total_cases -= 1
