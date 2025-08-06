import math

a = 0.75
total = 0
for i in range(25):
   total = (total/a)+500
   total = math.ceil(total)
   a = a+0.01
print(total)

#ans = 67259
