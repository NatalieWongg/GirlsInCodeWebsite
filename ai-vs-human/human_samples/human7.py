
odd = []
even = []
for x in numbers:
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
print (even + odd)