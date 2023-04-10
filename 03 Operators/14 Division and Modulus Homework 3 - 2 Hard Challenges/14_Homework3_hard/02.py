
days = int(input())

# By integer division over 360, we know how many 360s in the days
# Days should be: years * 360 + remaining_days
# //360 gives the years. %360 remove the year

years = days // 360
days = days % 360       # now we remove # of complete years. One easy way is mod

# same concept as above
months = days // 30
days = days % 30

print(years, months, days)
