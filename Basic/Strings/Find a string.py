'''Question:

You are given a string and a substring. Your task is to count the number of times the substring occurs in the given string. String traversal will take place from left to right, and the comparison should be case-sensitive. Write a Python program to accomplish this.

Input:

The first line of input contains the original string.
The second line contains the substring.
Output:

Print an integer, indicating the total number of occurrences of the substring in the original string.
'''
# Solution

# Define a function to count the number of occurrences of a substring in a string
def count_substring(original_string, substring):
    count = 0  # Initialize a count variable to keep track of the number of occurrences

    # Loop through the original_string, considering substrings of the same length as the given substring
    for i in range(len(original_string) - len(substring) + 1):
        # Check if the substring of the original_string (starting at index 'i' and ending at 'i + len(substring)')
        # is equal to the given 'substring'
        if original_string[i:i + len(substring)] == substring:
            count += 1  # If they match, increment the count

    return count  # Return the total count of occurrences

if __name__ == '__main__':
    original_string = input()  # Read the original string from the user
    substring = input()  # Read the substring from the user
    result = count_substring(original_string, substring)  # Call the function to count occurrences
    print(result)  # Print the result, which is the count of occurrences



'''For example, if the original string is 10 characters long and 
the substring is 3 characters long, we only need to check the first 8 characters to find the substring.'''
