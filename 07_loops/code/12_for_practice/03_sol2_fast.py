

n, m, w = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    for j in range(i, m + 1):
        k = i + j

        if 1 <= k <= w:
            cnt += w - k + 1

print(cnt)
