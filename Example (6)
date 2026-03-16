def simpleCipher(encrypted, k):
    decrypted = ""

    for letter in encrypted:
        index = ord(letter) - ord('A')
        new_index = (index - k) % 26
        decrypted += chr(new_index + ord('A'))

    return decrypted
