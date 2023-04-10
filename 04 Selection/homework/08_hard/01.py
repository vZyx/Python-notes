

x, s1, e1, s2, e2, s3, e3 = map(int, input().split())

#Read start and end, see if X is between them or not, times
cnt = 0
cnt += s1 <= x <= e1
cnt += s2 <= x <= e2
cnt += s3 <= x <= e3

print(cnt)
