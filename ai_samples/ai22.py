# Read input
nums = list(map(int, input().split()))

# Sort the numbers to make reasoning easier
nums.sort()

# The largest number must be A + B + C
total = nums[6]

# The smallest three numbers are candidates for A, B, and C
# Since total = A + B + C, we can find C by: C = total - A - B

A = nums[0]
B = nums[1]
C = total - A - B

# Output in ascending order
print(A, B, C)
