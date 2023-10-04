'''Question:

You are given a string, and your task is to change a character at a specific position within the string. Write a Python program that performs the following:

Define a function, mutate_string, that takes three arguments: string (the original string), position (the index to insert the character), and character (the character to insert).

Inside the function, convert the string into a list of characters to make it mutable.

Replace the character at the specified position with the new character.

Join the list of characters back into a string after making the modification.

Return the modified string.

In the main part of the code, read the original string, the position, and the character to insert from the user.

Call the mutate_string function to perform the modification.

Print the modified string.

Input:

The first line contains a string, string, representing the original string.
The second line contains an integer, position, representing the index location where the character needs to be inserted.
The third line contains a string, character, representing the character to insert.
Output:

Print the modified string after changing the character at the specified position.'''

# Solution

# Define a function to mutate a string by changing a character at a specified position
def mutate_string(string, position, character):
    # Convert the input string into a list of characters to allow modifications
    string_list = list(string)
    
    # Replace the character at the specified position with the new character
    string_list[position] = character
    
    # Join the list of characters back into a string
    modified_str = ''.join(string_list)
    
    return modified_str

if __name__ == '__main__':
    # Read the original string
    s = input()
    
    # Read the position and the character to insert, separated by a space
    i, c = input().split()
    
    # Call the 'mutate_string' function to modify the string
    s_new = mutate_string(s, int(i), c)
    
    # Print the modified string
    print(s_new)

