def character_frequency_difference(s: str) -> int:
    from collections import Counter

    # Count frequency of each character (case-sensitive)
    freq = Counter(s)

    # Get max and min frequency values
    max_freq = max(freq.values())
    min_freq = min(freq.values())

    return max_freq - min_freq

# Example usage
input_str = "aaabbbbc"
result = character_frequency_difference(input_str)
print("Output:", result)
