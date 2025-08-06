def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
input1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 3, 9, 10, 4, 11, 12, 6, 13, 14, 15, 8, 16, 17, 18, 9, 19, 20]
input2 = [5, 8, 12, 5, 7, 12, 15, 8, 19, 22, 5, 7, 23, 25, 26, 27, 19, 30, 31, 8, 33, 35, 36, 25, 37, 38, 39, 40, 41, 33, 42, 43, 44, 45, 46, 30, 47, 48, 49, 50, 51, 52, 53, 54, 45, 55, 56, 57, 58, 59, 60, 61, 33, 63, 64, 65, 66, 67, 45]
input3 = [38, 38, 6, 23, 32, 9, 24, 25, 15, 7, 23, 26, 20, 7, 10, 28, 29, 37, 25, 11, 28, 33, 19, 9, 23, 35, 37, 23, 9, 20, 35, 30, 5, 9, 29, 31, 21, 9, 26, 20, 3, 39, 9, 8, 3, 10, 20, 19, 31, 13, 12, 8, 26, 14, 16, 29, 34, 25, 21, 16, 36, 5, 39, 6, 22, 37, 25, 9, 28, 33, 4, 11, 22, 0, 12, 1, 30, 25, 2, 17, 17, 8, 28, 30, 16, 27, 18, 7, 15, 23, 35, 32, 38, 3, 37, 33, 27, 31, 8, 6, 21, 32, 21, 14, 9]

print("Output 1:", remove_duplicates_preserve_order(input1))
print("Output 2:", remove_duplicates_preserve_order(input2))
print("Output 3:", remove_duplicates_preserve_order(input3))
