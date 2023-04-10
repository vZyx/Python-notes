
nb, ng, nt = map(int, input().split())

# nb greater than 25
print(nb > 25)

# ng less than or equal to 30_oop
print(ng <= 30)

#     nb > 20 and nt > 2 or ng > 30_oop and nt > 4
print(nb > 20 and nt > 2 or ng > 30 and nt > 4)

# Either nb < 60 or ng < 70
print(nb < 60 or ng < 70)

# Neither nb >= 60 nor ng >= 70
print(  not nb >= 60 and not ng >= 70 )

# nb is 10 more students than ng
print(nb == ng + 10)

# Difference between nb and ng is more than 10 or nt > 5
print(nb - ng > 10 or nt > 5)

# Either nb is 10 more students than ng or ng is 15 more students than nb
print(nb == ng + 10 or ng == nb + 15)

