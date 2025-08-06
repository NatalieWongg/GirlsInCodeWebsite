def sum_of_positive_integers(lst):
    return sum(num for num in lst if num > 0)

# Example usage
input_list = [1, 3, 2, -5]
print("Output:", sum_of_positive_integers(input_list))
