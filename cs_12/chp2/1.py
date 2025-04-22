'''
Write a Python program to print the ASCII values of all lowercase and uppercase letters in the English alphabet.
The program should output the character and its corresponding ASCII value for each letter from 'a' to 'z' and 'A' to 'Z'.
Example Output :
Character: a, ASCII Value: 97
Character: b, ASCII Value: 98
...
Character: Z, ASCII Value: 90
'''
# Print ASCII values for lowercase letters
print("Lowercase Letters:")
for char in range(ord('a'), ord('z') + 1):
    print(f"Character: {chr(char)}, ASCII Value: {char}")

# Print ASCII values for uppercase letters
print("\nUppercase Letters:")
for char in range(ord('A'), ord('Z') + 1):
    print(f"Character: {chr(char)}, ASCII Value: {char}")