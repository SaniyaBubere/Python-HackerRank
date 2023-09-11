'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0
is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1
'''

# Solution

if __name__ == '__main__':
    # Read an integer from the user
    n = int(input().strip())

    # Check if n is odd
    if n % 2:
        print("Weird")  # If n is odd, print "Weird"
    # Check if n is even and in the range (2, 5)
    elif n > 2 and n < 5:
        print("Not Weird")  # If n is even and in the range (2, 5), print "Not Weird"
    # Check if n is even and in the range (6, 20)
    elif n > 6 and n <= 20:
        print("Weird")  # If n is even and in the range (6, 20), print "Weird"
    else:
        print("Not Weird")  # If n doesn't meet any of the above conditions, print "Not Weird"
