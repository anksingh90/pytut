'''
Given a string s, you need to check if it is palindrome or not.(A palidrome is a string that reads the same from front and back.)
Input: s = "Hello"	# Hello = olleH
Output: false
Input: s = "TenEt"	# TenEt = tEneT
Output: true
'''
s = input('Enter a string : ')
s_lower = s.lower()  # Convert the string to lowercase
is_palindrome = s_lower == s_lower[::-1]

print(f"'{s}' is palindrome: {is_palindrome}")