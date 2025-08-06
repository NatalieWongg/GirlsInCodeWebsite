def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Example usage
input_list = [1, 4, 7, 8, 10]
result = sum_of_even_numbers(input_list)
print("Output:", result)
