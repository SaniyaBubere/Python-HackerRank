'''Task: Text Wrapping

You are given a long string and a maximum width. Your task is to wrap the string into paragraphs of the specified width.

Write a Python function called wrap that takes two parameters:

string: A long string.
max_width: An integer representing the maximum width for wrapping.
The function should return a single string with newline characters ('\n') where the breaks should be.

Input Format:

The function should take input from two parameters: string (a long string) and max_width (an integer representing the maximum width for wrapping).

Output Format:

The function should return a single string with newline characters ('\n') where the breaks should be.'''

# solution

import textwrap

# Define a function to wrap the input string to the specified width
def wrap(string, max_width):
    # Use textwrap.fill to wrap the string
    wrapped_text = textwrap.fill(string, max_width)
    return wrapped_text

if __name__ == '__main__':
    # Get the input string and maximum width from the user
    string = input("Enter the string: ")
    max_width = int(input("Enter the maximum width: "))
    
    # Call the wrap function to wrap the string
    result = wrap(string, max_width)
    
    # Print the wrapped text
    print(result)


or import textwrap
 
def wrap(string, max_width):
    warraped_text=textwrap.fill(string,max_width)
    return warraped_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

