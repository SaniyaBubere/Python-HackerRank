'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''

# Solution

# Read the number of students
n = int(input())

# Create an empty dictionary to store student names and their marks
student_marks = {}

# Populate the dictionary with student names and marks
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    student_marks[name] = marks

# Read the name of the student for which you want to calculate the average
query_name = input()

# Get the list of marks for the queried student
marks_list = student_marks[query_name]

# Calculate the average of the marks
average_marks = sum(marks_list) / len(marks_list)

# Print the average with 2 decimal places
print("{:.2f}".format(average_marks))
