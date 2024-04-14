# Your solution to Exercise 3
def countdown(n):
    for num in range(20, n+1):
        print(num, end=" ")

n = int(input())
countdown(n)

# Same issue here:
# Function naming, parameter naming, and type hinting.