def bacteria_growth(b, m, r):
    days = 0
    while b < m:
        b += b * r
        days += 1
    return days

# Given input values
b = 1000.076893438  
m = 7897654345678965345678907654323456789876534567432345698767890987.987678  
r = 0.3758938726  

# Compute the result
days = bacteria_growth(b, m, r)
print(days)