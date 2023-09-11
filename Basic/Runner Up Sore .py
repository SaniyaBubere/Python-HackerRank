'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[]  of n integers each separated by a space.'''

# Solution

# Read the number of participants
n = int(input())

# Read the list of scores as a space-separated string and convert it into a list of integers
arr = list(map(int, input().split()))

# Remove duplicates from the list by converting it to a set
duplicate_element_remove = set(arr)

# Sort the set of unique scores in ascending order
sorting_unique_ele = sorted(duplicate_element_remove)

# Print the second-to-last element in the sorted list, which is the runner-up score
print(sorting_unique_ele[-2])
