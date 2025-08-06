def decrypt_tome(pages):
    decrypted = []

    for num in pages:
        reversed_num = int(num[::-1])  # Reverse and convert to int
        mod_val = reversed_num % 26
        letter = chr(ord('A') + mod_val)  # Map 0→A, 1→B, ..., 25→Z
        decrypted.append(letter)

    return ''.join(decrypted)

# Example usage
pages = ['812', '461', '98', '17']
result = decrypt_tome(pages)
print("Decrypted message:", result)
