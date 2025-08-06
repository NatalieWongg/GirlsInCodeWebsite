def nth_char_from_end(s, n):
    if n <= 0 or n > len(s):
        return "Invalid input"
    return s[-n]

# Example usage
s = "abcdef"
n = 3
print("Output:", nth_char_from_end(s, n))
