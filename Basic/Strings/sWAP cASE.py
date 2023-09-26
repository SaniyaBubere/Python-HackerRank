# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# Solution

# Define a function to swap the cases of characters in a string
def swap_case(s):
    # Initialize an empty string to store the result
    result = ''

    # Iterate through each character in the input string 's'
    for char in s:
        # Check if the character is uppercase and convert to lowercase if so
        if char.isupper():
            result += char.lower()
        # Check if the character is lowercase and convert to uppercase if so
        elif char.islower():
            result += char.upper()
        else:
            # If the character is not a letter (e.g., a symbol or digit), add it as is
            result += char

    return result

if __name__ == '__main__':
    # Read the input string
    s = input()

    # Call the 'swap_case' function to swap the cases of characters in 's'
    result = swap_case(s)

    # Print the modified string with swapped cases
    print(result)
