'''Question:

You are given a string s. Your task is to determine if the string contains the following:

Alphanumeric characters.
Alphabetical characters.
Digits.
Lowercase characters.
Uppercase characters.
Write a Python program to perform these checks and print the results.

Input:

A single line containing a string s.
Output:

In the first line, print True if s has any alphanumeric characters; otherwise, print False.
In the second line, print True if s has any alphabetical characters; otherwise, print False.
In the third line, print True if s has any digits; otherwise, print False.
In the fourth line, print True if s has any lowercase characters; otherwise, print False.
In the fifth line, print True if s has any uppercase characters; otherwise, print False.'''

# Solution



if __name__ == '__main__':
    s = input()  # Read the input string from the user

    # Initialize variables to store the results of string validation checks
    has_alphanumeric = False
    has_alphabetical = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    # Iterate through each character in the input string
    for char in s:
        if char.isalnum():
            has_alphanumeric = True
        if char.isalpha():
            has_alphabetical = True
        if char.isdigit():
            has_digits = True
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True

    # Print the results for each validation check
    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)


o/p : Hacker123

