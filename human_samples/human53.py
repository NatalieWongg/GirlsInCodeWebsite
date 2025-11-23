

sum = 0
for i in range(1, 101):
    sum+=i**2

sum2=0
for z in range(1, 101, 10):
    group = list(range(z, z+10))
    for y in range(group):
        sum2+=y*y 

a = sum - sum2
print(a)