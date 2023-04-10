
print( (1 + 2) * (3 + 1) / 2)

n = int(input())
ans = (n * (n + 1)) / 2


"""
Why such equation?
Here is an intuition for N = 8
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

Let's arrange as following
1 8   2 7    3 6     4 5       [first number and last number]   [2nd number, and 2nd from back] ...

What is the value of each pair? 9 = n+1
How many pairs? 4 = n/2

So n/2 pair, each has value n+1
So total sum is (n * (n+1))/2

Now, this works for even N
Your turn: why works for odd N

More readings: http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html
"""
