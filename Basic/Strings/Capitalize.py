'''Problem Statement: Capitalize Words in a String

You are given a string consisting of words separated by spaces. Your task is to capitalize the first letter of each word and return the modified string.

Write a Python function called capitalize_words that takes a string as input and returns the string with the first letter of each word capitalized. Implement the function and use it to process the input.

Function Signature: def capitalize_words(s: str) -> str

Input:

A string s (1 <= len(s) <= 1000): The input string containing words separated by spaces. The string may contain alphabetic characters, spaces, and may consist of both lowercase and uppercase letters.
Output:

A string: The input string with the first letter of each word capitalized.'''

# Solution

def solve(s):
    # x = s.title()
    # return x
    return ' '.join(word.capitalize() for word in s.split(' '))
