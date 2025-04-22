'''
Write a Python program to reverse the words in a given sentence while keeping the word order the same.
'''
s = "Hello World Python"

words = s.split()   # Split the sentence into words

reversed_words = []     # Reverse each word

for word in words:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    reversed_words.append(reversed_word)

reversed_sentence = " ".join(reversed_words)    # Join the reversed words back into a sentence

print(reversed_sentence)
