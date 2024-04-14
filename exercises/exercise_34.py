# Your solution to Exercise 34
def pattern(n):
    str_num = ""
    for i in range(1, n+1):
        for j in range(1, i+1):
            str_num += str(j)
        print(str_num)
        str_num = ""

n = int(input())
pattern(n)

# Same Issue:
# Function naming, parameter naming, and type hinting.

# Notes:
# Managed to trick out the test cases by using a string to store the numbers :D 
# But well done in general. Get familiar with expected solution.