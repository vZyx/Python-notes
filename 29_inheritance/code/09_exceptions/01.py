
# All True
print(issubclass(Exception, BaseException))
print(issubclass(ArithmeticError, BaseException))
print(issubclass(ArithmeticError, Exception))
print(issubclass(ZeroDivisionError, ArithmeticError))
print(issubclass(PermissionError, Exception))

print(issubclass(SystemExit, Exception))        # False
print(issubclass(SystemExit, BaseException))    # True


