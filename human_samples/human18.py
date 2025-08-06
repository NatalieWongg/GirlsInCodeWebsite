c1, m1 = 695789, 393585
c2, m2 = 705404, 502652
c3, m3 = 999933, 95061


for i in range(100):
    transfer = min(m1, c2 - m2)
    m1 -= transfer
    m2 += transfer
    
    transfer = min(m2, c3 - m3)
    m2 -= transfer
    m3 += transfer
    
    transfer = min(m3, c1 - m1)
    m3 -= transfer
    m1 += transfer

print(m1)
print(m2)
print(m3)