# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Solution

# Define a function to split a string on spaces and join using hyphens
def split_and_join(line):
    # Use the 'split()' method to split the input 'line' on spaces and create a list of words
    words = line.split(" ")

    # Use the 'join()' method to join the words with hyphens to create a modified string
    result = "-".join(words)

    # Return the modified string
    return result

if __name__ == '__main__':
    # Read the input line
    line = input()

    # Call the 'split_and_join' function to process the input line
    result = split_and_join(line)

    # Print the modified string with hyphens replacing spaces
    print(result)

# OR

def split_and_join(line):
    # write your code here

    result = "-".join(line.split(" "))
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
