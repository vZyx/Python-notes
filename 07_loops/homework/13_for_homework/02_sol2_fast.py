cnt = 0

for x in range(50, 301):
    '''
    Let's speed it
    We can always start from the right condition maximum(70, x+1)
        Saves some Y iterations
        Remove the x < y condition
    '''
    start = max(70, x+1)

    for y in range(start, 401):
        if (x + y) % 7 == 0:
            cnt += 1

print(cnt)
