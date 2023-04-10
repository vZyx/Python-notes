

"""
Let's print the upper triangle first
Let's assume N = 4, how many spaces and starts we print
Row 1	Spaces 3	Stars 1
Row 2	Spaces 2	Stars 3
Row 3	Spaces 1	Stars 5
Row 4	Spaces 0	Stars 7

Now we wanna develop formulas for number of spaces and number of starts
For a given 'row'
Spaces are: N - rows   	(3, 2, 1, 0)
Starts are: 2*row -1	(1, 3, 5, 7)

Now we just iterate for each row
print spaces
then print starts
"""


n = int(input())


row = 1
while row <= n:
    # Print N - rows spaces
    stars_count = 1
    while stars_count <= n - row:
        print(' ', end='')
        stars_count += 1

    # Print 2*rows-1 spaces
    stars_count = 1
    while stars_count <= 2 * row-1:
        print('*', end='')
        stars_count += 1

    print()
    row += 1


row = n
while row > 0:
    # Print N - rows spaces
    stars_count = 1
    while stars_count <= n - row:
        print(' ', end='')
        stars_count += 1

    # Print 2*rows-1 spaces
    stars_count = 1
    while stars_count <= 2 * row-1:
        print('*', end='')
        stars_count += 1

    print()
    row -= 1

