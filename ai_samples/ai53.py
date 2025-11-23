import math
numbers =  [1024, 1280, 1920]
gcd = 1024
for i in numbers[1:]:
    gcd = math.gcd(gcd, i)
print(gcd)
