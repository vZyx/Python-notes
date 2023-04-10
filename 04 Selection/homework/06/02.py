
a, b, c = map(int, input().split())

# To understand: apply on 3 2 1

if b < a:  # Swap them:
    a, b = b, a

# Now a and b are in correct order: e.g. 2 3 1

if c < b:  # Swap them
    b, c = c, b

    # Now b, are correct
    # But a, may not be again with b: e.g. 2 1 3

    if b < a:      # Swap them
        a, b = b, a

        # Now 1 2 3

print(a, b, c)