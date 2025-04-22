'''
Given a string S, the task is to determine whether the string starts and ends with the characters 'abc' (case insensitive).
Input:
S: "aBc1234ABC"
Output:
Yes
'''

S = "aBc1234ABC"
S_lower = S.lower()  # Convert the string to lowercase

if S_lower[:3] == 'abc' and S_lower[-3:] == 'abc':
    print("Yes")
else:
    print("No")