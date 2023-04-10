

result = 0
n = int(input())

cnt = 0

while cnt <= n:
    if cnt % 8 == 0 or cnt % 3 == 0 and cnt % 4 == 0:
        print(cnt, end=' ')

    cnt += 1
