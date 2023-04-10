

# Based on English Dictionary
# Letter by letter comparison

# If a word has a smaller letter: it appears first
print('love' < 'zebra') # True  l is before z
print('love' < 'long')  # False: lo are common, but v > n
print('love' != 'long') # True

# If one word is done in comparison: the smaller in length comes first
print('counter' < 'counterattack')  # True

# Upper letters are smaller than small letters
print('A' < 'a')            # True
print('A' < 'z')            # True
print('Z' < 'a')            # True
print('loVE' < 'love')      # True V < v
print('loVE' < 'long')      # True V < n

print('' < 'A')             # True empty is smaller

print(' ' < 'A')            # True: space smaller than letters
print(' ' < 'a')            # True: space smaller than letters

print('0' < 'A')            # True: Digits smaller than letters
print('0' < 'a')            # True: Digits smaller than letters

