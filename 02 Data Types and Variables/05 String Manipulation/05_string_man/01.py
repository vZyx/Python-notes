

print('I am mostafa')               # I am mostafa
print('I am' + ' ' + 'mostafa')     # I am mostafa

str1 = 'I am'
str2 = ' mostafa'
print(str1 + str2)                  # I am mostafa

print(str1 * 3)             # I amI amI am
print(2 * str1 + str2)      # I amI am mostafa

str1 = 'Hello '
str3 = str1 + str2 + str1
print(str3)                 # Hello  mostafaHello


# \t is escape character for TAB
# A Tab character shifts over to the next tab stop.
# By default, there is one every 8 spaces.
print('1234567890123456789')   # 1234567890123456789
print('Hello\tworld')           # Hello   world
print('Hello\t\tworld')         # Hello           world