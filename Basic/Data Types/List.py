'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands 
where each command will be of the  types listed above. Iterate through each command in order and 
perform the corresponding operation on your list.'''

# SOlution

# Initialize an empty list
my_list = []

# Read the number of commands
n = int(input())

# Loop through each command
for _ in range(n):
    # Read the command as a space-separated string and split it into words
    command = input().split()
    
    # Check the first word in the command to determine which operation to perform
    if command[0] == "insert":
        # If it's an "insert" command, extract the values i and e
        i, e = map(int, command[1:])
        # Insert the integer e at position i in the list
        my_list.insert(i, e)
    elif command[0] == "print":
        # If it's a "print" command, print the current state of the list
        print(my_list)
    elif command[0] == "remove":
        # If it's a "remove" command, extract the value e to remove from the list
        e = int(command[1])
        # Remove the first occurrence of integer e from the list
        my_list.remove(e)
    elif command[0] == "append":
        # If it's an "append" command, extract the value e to append to the list
        e = int(command[1])
        # Append the integer e to the end of the list
        my_list.append(e)
    elif command[0] == "sort":
        # If it's a "sort" command, sort the list in ascending order
        my_list.sort()
    elif command[0] == "pop":
        # If it's a "pop" command, remove the last element from the list
        my_list.pop()
    elif command[0] == "reverse":
        # If it's a "reverse" command, reverse the order of elements in the list
        my_list.reverse()
