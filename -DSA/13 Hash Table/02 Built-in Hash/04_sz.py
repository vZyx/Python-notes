
import sys

print(sys.hash_info.width)  # 64 = 8 bytes x 8 bits
print(sys.maxsize)          # 9223372036854775807

# maxsize = largest value to store in Py_ssize_t data type
# 32-bit: the value will be 2^31 – 1, i.e. 2147483647
# 64-bit: the value will be 2^63 – 1, i.e. 9223372036854775807

print(hash(2 ** 100))       # 549755813888
print(hash('abc' * 50) )    # -300961300000803550

