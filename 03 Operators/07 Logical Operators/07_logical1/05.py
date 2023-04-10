
# both expressions evaluated
print(2 > 10 or 5 < 6)      # True

# Expression 5 < 6 will be discarded
print(2 < 10 or 5 < 6)      # True

# Expression 3 < 6 will be discarded
print(2 > 10 and 3 < 6 or 3 > 4)    # False

