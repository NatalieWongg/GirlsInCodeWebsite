def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2

# Example usage:
nums = [7, 3, 1, 4, 9, 6]
median = find_median(nums)
print("Median:", median)
