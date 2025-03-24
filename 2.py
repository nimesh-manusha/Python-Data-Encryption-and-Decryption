def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u",]
    count = 0
    for char in s.lower():  
        if char in vowels:
            count += 1 
    return count

print(count_vowels("HEllo my parents"))  
print(count_vowels("Mother"))       
print(count_vowels("LAPTOP"))       
