import re
import string

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    
    for word in words:
        # Remove leading/trailing punctuation
        cleaned = word.strip(string.punctuation)

        # Skip if it contains any digits
        if re.search(r'\d', cleaned):
            continue

        # Check if it's the new longest word
        if len(cleaned) > len(longest):
            longest = cleaned

    return longest

# Example usage
input_sentence = "The quick brown fox jumps over the lazy dog"
print("Output:", longest_word(input_sentence))
