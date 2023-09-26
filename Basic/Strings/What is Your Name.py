'''Write a Python program that takes two strings as input: a first name and a last name. Create a message that says "Hello [first name] [last name]! 
You just delved into python." and print this message.'''

# Solution

# Define a function to print a full name message
def print_full_name(first, last):
    # Create a message by formatting the first and last names
    message = f'Hello {first} {last}! You just delved into python.'
    
    # Print the formatted message
    print(message)

if __name__ == '__main__':
    # Read the first name from the user
    first_name = input()
    
    # Read the last name from the user
    last_name = input()
    
    # Call the 'print_full_name' function to print the full name message
    print_full_name(first_name, last_name)
