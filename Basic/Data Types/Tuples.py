'''Write a Python program that takes an integer, n, as input representing the number of elements, followed by n space-separated integers. 
Create a tuple from these integers and calculate the hash value of the tuple. Print the resulting hash value.'''

# Solution

# Read the number of elements in the tuple
n = int(input())

# Read space-separated integers and create a tuple from them
integer_tuple = tuple(map(int, input().split()))

# Calculate the hash value of the tuple
result = hash(integer_tuple)

# Print the hash value
print(result)
