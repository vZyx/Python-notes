n = int(input())

cnt = 0
current_number = 0

while cnt < n:
    if current_number % 3 == 0 and current_number % 4 != 0:
        print(current_number, end=' ')
        cnt += 1

    current_number += 1
