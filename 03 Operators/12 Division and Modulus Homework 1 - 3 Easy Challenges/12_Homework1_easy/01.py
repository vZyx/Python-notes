
a1, a2, a3, a4, a5 = map(float, input().split())

avg1 = (a1 + a2 + a3 + a4 + a5) / 5.0   # A
sum1 = (a1 + a2 + a3) / (a4 + a5)       # B
first3_avg = (a1 + a2 + a3) / 3.0
last2_avg = (a4 + a5) / 2.0
avg2 = first3_avg / last2_avg           # C

print(avg1, sum1, avg2)
print(sum1 * 2/3)                       # C = 2/3 B
