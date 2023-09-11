'''Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.'''

# Solution

# Read an integer 'n' from the user
n = int(input())

# Start a loop that iterates from 0 to (n-1)
for i in range(0, n):
    # Inside the loop, calculate the square of 'i' using the exponentiation operator '**'
    square = i ** 2

    # Print the square value
    print(square)
  
