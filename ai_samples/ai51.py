import math

# Calculate the LCM of numbers from 1 to 20
lcm = math.lcm(*range(1, 21))

print(f"The smallest number evenly divisible by all numbers from 1 to 20 is: {lcm}")
