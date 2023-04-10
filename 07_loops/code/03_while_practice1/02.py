

num, pow = map(int, input().split())

pyhon_result = num ** pow

our_result = 1

while pow >= 1:
    our_result *= num
    pow -= 1

print(our_result)

assert pyhon_result == our_result, 'Hmm'

