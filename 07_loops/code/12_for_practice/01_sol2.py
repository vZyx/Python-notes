

total_cases = int(input())

for case in range(total_cases):
    N, sum = int(input()), 0

    for pos in range(N):
        value = int(input())
        sum += value ** (pos+1)

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