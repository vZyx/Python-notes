# We need 3 nested loops
# loop over test cases
#   loop over reading numbers
#       loop to repeat the number K times (multiplication)


T = int(input())
# Loop on cases
while T > 0:
    N = int(input())
    cnt_N, sum = 1, 0

    # loop over reading a case
    while cnt_N <= N:
        value = int(input())
        cnt_deep, result = cnt_N, 1

        # Loop to compute the sum: a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……
        while cnt_deep > 0:
            result *= value
            cnt_deep -= 1

        sum += result
        cnt_N += 1

    print('Sum is', sum)
    T -= 1


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