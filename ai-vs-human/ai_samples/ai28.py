import re
from collections import Counter

def word_ratio(filename):
    # Read file content
    with open(filename, 'r') as file:
        text = file.read()

    # Normalize text: lowercase and extract words only
    words = re.findall(r'\b\w+\b', text.lower())

    # Count word frequencies
    word_counts = Counter(words)

    # Find the most common word's count
    max_count = max(word_counts.values())

    # Get number of distinct words
    unique_word_count = len(word_counts)

    # Calculate ratio and round to 3 decimal places
    ratio = round(max_count / unique_word_count, 3)

    return ratio

# Example usage (assuming the input is in 'input.txt'):
# Save the input text into 'input.txt' before running this.
print(word_ratio('input.txt'))
