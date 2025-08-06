def count_words(s):
    import re
    # Define the punctuation characters
    punctuation = [' ', ',', '.', '!', '?', '-']
    # Create a regex pattern using the punctuation list
    pattern = '[' + re.escape(''.join(punctuation)) + ']+'
    # Split the string using the pattern and filter out empty strings
    words = [word for word in re.split(pattern, s) if word]
    return len(words)