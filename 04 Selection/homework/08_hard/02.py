s1, e1, s2, e2 = map(int, input().split())

if e1 < s2 or e2 < s1:
    print(-1)		# One of them ends before start of the another
else:
    # This is tricky. Trying to list all cases will be hard and buggy
    # You need to notice which ones came first
    # Then consider the possible cases (e.g. one of them completely inside the second)

    # However, thinking makes it easier
    # The intersection starts at the maximum of the starts
    # The intersection ends at the minimum of the ends
    # Draw some examples

    if s1 < s2:
        s1 = s2	    # maximum of (s1, s2)
    if e1 > e2:
        e1 = e2	    # minimum of (e1, e2)

    print(s1, e1)

'''
Cases
1 15  20 30_oop		==> -1
20 30_oop 1 15		==> -1
1 6    1 6		==> 1 6
1 6    1 3		==> 1 3
1 6    2 3		==> 2 3
1 6    3 8		==> 3 6
3 8    1 6		==> 3 6
'''