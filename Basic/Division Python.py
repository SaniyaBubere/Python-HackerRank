'''Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example


The result of the integer division .
The result of the float division is .
Print:

0
0.6
Input Format

The first line contains the first integer, .
The second line contains the second integer, .'''

# Solution

# Read the first integer from the user
a = int(input())

# Read the second integer from the user
b = int(input())

# Perform integer division of 'a' by 'b' and store the result in 'c'
c = a // b

# Perform float division of 'a' by 'b' and store the result in 'd'
d = a / b

# Print the result of integer division
print(c)

# Print the result of float division
print(d)
