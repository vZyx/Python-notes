x, a1, a2, a3, a4, a5 = map(float, input().split())
cnt = 0

# We can use if else, but for educational purpose:
cnt += a1 <= x
cnt += a2 <= x
cnt += a3 <= x
cnt += a4 <= x
cnt += a5 <= x

# clearly the 2 values just complement each others
print(cnt, 5 - cnt)

