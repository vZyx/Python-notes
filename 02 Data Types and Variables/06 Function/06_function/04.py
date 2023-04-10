

msg_str = '10'
xint = int(msg_str)
xflo = float(msg_str)

print(msg_str, type(msg_str))   # 10 <class 'str'>
print(xint, type(xint))         # 10 <class 'int'>
print(xflo, type(xflo))         # 10.0 <class 'float'>

my_float = 20.7
my_int = int(my_float)
msg = str(my_float)

print(my_float, type(my_float)) # 20.7 <class 'float'>
print(my_int, type(my_int))     # 20 <class 'int'>   observe loss of .7
print(msg, type(msg))           # 20.7 <class 'str'>

# Tip: Don't use variable name same as function name
# such as int, str, len, min, max, etc

# ValueError (A run time error)
print(int('hello'))