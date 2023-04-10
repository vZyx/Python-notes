
x = -5
if x:
    print(x, 'is considered True')  # printed

x = ''
if not x:
    print(x, 'is considered False')  # printed

print(5 or 7)               # 5
print(0 or 7)               # 7
print(0 and 7)              # 0

print(5 and 7 and 10)       # 10
print(5 or 7 or 10)         # 5
print(0 or 5 or 7 or 10)    # 5

print('' or 0)              # 0
print(0 or '')              # Empty str ''

