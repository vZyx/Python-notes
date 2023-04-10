

class A:
   def __init__(self, b):
       self.b = b

   def __del__(self):
       print('deleting A')


class B:
   def __init__(self, a):
       self.a = a

   def __del__(self):
       print('deleting B')


a = A(None)
b = B(a)
a.b = b

import sys
print(sys.getrefcount(a)-1)     # 2
print(sys.getrefcount(b)-1)     # 2
# deleting A deleting B

