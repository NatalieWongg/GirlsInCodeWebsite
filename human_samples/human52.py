a1 = 1
a2 = 2
an = a1 + a2
sum = 2
while an <= 4000000:
    if an % 2 ==0:
        sum += an
    a1 = a2
    a2 = an
    an = a1 + a2
print(sum)
