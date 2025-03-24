def encrypt(text):
    """Encrypts the given text using Caesar cipher (shift 3) and reverses it."""
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + 3)
        encrypted_text += encrypted_char
    return encrypted_text[::-1] 
def decrypt(encrypted_text):
    """Decrypts the given encrypted text by reversing and applying Caesar cipher (shift -3)."""
    decrypted_text = ""
    reversed_text = encrypted_text[::-1] 
    for char in reversed_text:
        decrypted_char = chr(ord(char) - 3)
        decrypted_text += decrypted_char
    return decrypted_text

if __name__ == "__main__":
    password = input("Enter the password: ")

    encrypted_password = encrypt(password)
    print("Encrypted password:", encrypted_password)

    decrypted_password = decrypt(encrypted_password)
    print("Decrypted password:", decrypted_password)

    print("\n --run--123")
    print("Empty string encryption:", encrypt(""))
    print("Special characters encryption:", encrypt("!@#$%^"))
