'''Question:

Ms. Gabriel Williams, a botany professor at District College, is conducting a research project on plant heights in her greenhouse. She asked her student Mickey to calculate the average height of plants with distinct heights. Can you help Mickey write a Python program to achieve this task?

Write a Python function average(arr) that takes a list of integers as input and returns the average of distinct heights rounded to three decimal places. The function should perform the following steps:

Create a set to store distinct heights.
Calculate the sum of distinct heights.
Count the number of distinct heights.
Calculate the average by dividing the total height by the count of distinct heights.
Round the average to three decimal places and return it.
Write a complete Python program to solve this problem. Read the input as follows:

The first line contains an integer n, the number of plant heights.
The second line contains n space-separated integers, which represent the heights of plants.
Your program should calculate and print the average of distinct plant heights.

Input:

The first line contains an integer n (1 <= n <= 100), the size of the list of plant heights.
The second line contains n space-separated integers (1 <= height <= 10^3), representing the heights of the plants.'''

# solution

def average(array):
    # your code goes here
    distinct_heights = set(arr)  # Create a set to store distinct heights
    total_height = sum(distinct_heights)  # Calculate the sum of distinct heights
    count = len(distinct_heights)  # Count the number of distinct heights
    avg = total_height / count  # Calculate the average
    return round(avg, 3)  # Round the average to 3 decimal places


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
