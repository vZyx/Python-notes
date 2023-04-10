

class StrNoAllowed1:
    pass


#TypeError: exceptions must derive from BaseException
#raise StrNoAllowed1


# You must extend from built-in exceptions
class StrNoAllowed2(BaseException):
    pass

raise StrNoAllowed2