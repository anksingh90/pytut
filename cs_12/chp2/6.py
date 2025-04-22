'''
Write a Python program to find the first non-repeating character in a given string.
'''
s = "aabbc"
char_freq = {}

# Count the frequency of each character
for char in s:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Find the first non-repeating character
for char in s:
    if char_freq[char] == 1:
        print(f"The first non-repeating character is: {char}")
        break
else:
    print("No non-repeating character found")