def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 1:
        return sorted_lst[mid]
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

# Example usage
input_list = [2, 7, -5, 5]
print("Output:", find_median(input_list))
