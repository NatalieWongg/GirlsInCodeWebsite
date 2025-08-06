def count_multiples_of_11(lst):
    return sum(1 for num in lst if num % 11 == 0)

# Example usage
input_list = [22, 7, 1, 121, 11]
print("Output:", count_multiples_of_11(input_list))
