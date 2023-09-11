'''The included code stub will read an integer,n , from STDIN.

Without using any string methods, try to print the following:
1234....n
Note that "..." represents the consecutive values in between.

Example
n=5
print string 12345
Print the string .'''

# Solution

# Read an integer 'n' from the user
n = int(input())

# Start a loop that iterates from 1 to 'n' (inclusive)
for i in range(1, n + 1):
    # Inside the loop, print the value of 'i' without a newline character
    print(i, end='')

# The 'end=""' argument in the print function ensures that there is no newline character after each print statement,
# so the numbers will be printed on the same line.

# The loop will print the numbers from 1 to 'n' without any spaces or line breaks between them.
