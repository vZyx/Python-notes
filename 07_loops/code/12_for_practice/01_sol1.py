
total_cases = int(input())

for case in range(total_cases):
    N, sum = int(input()), 0

    for pos in range(N):
        value, result = int(input()), 1

        # Loop to compute the sum: a, b*b, c*c*c
        for it in range(pos + 1):
            result *= value

        sum += result

    print('Sum is', sum)

"""
input
2
3   
5 
7 
2
4  
1 
2 
3 
4


"""