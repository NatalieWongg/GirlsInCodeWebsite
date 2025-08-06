def sum_of_harshad_numbers(start: int, end: int) -> int:
    def is_harshad(n: int) -> bool:
        digit_sum = sum(int(digit) for digit in str(n))
        return digit_sum != 0 and n % digit_sum == 0

    harshad_sum = 0
    for number in range(start, end + 1):
        if is_harshad(number):
            harshad_sum += number

    return harshad_sum

# Example usage
start = 2
end = 20
result = sum_of_harshad_numbers(start, end)
print("Sum of Harshad numbers:", result)
