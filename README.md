focuses on:
Algorithm design with constraints
Debugging and fixing logical errors
Code tracing and prediction
Efficiency analysis and optimization

Section A: Problem-Solving & Programming
Question 1: Data Encryption and Decryption

Problem Statement:
A company wants to securely store user passwords by encrypting them using a custom algorithm before storing them in a database. You must implement both encryption and decryption functions.

Encryption Rules:
Replace each character with its ASCII value + 3 (Caesar cipher with shift 3).
Reverse the encrypted string.

Decryption Rules:
Reverse the encrypted string.
Subtract 3 from each character’s ASCII value to retrieve the original text.

Tasks:
Implement the encrypt(text) and decrypt(encrypted_text) functions.
Ensure the program handles uppercase, lowercase, and numeric characters.
Allow the user to input a password and display the encrypted and decrypted versions.
Test the program with edge cases, such as empty strings and special characters.
