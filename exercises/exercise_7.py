# Your solution to Exercise 7
def pattern(n):
    for i in range(1, n+1):
        print("#" + (" " * (i-1)) + "#")
n = int(input())
pattern(n)

# Same issue here:
# Function naming, parameter naming, and type hinting.