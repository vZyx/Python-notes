n, m = map(int, input().split())

cnt_n = 1

# first col loop
while cnt_n <= n:
    cnt_m = 1

    # second col loop
    while cnt_m <= m:
        print(cnt_n, " x ", cnt_m, " = ", cnt_n * cnt_m)
        cnt_m += 1

    cnt_n += 1
