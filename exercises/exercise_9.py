# Your solution to Exercise 9
def multiples(a,b,c):
    for i in range(a, b+1):
        if i % c != 0:
            continue
        if i == b-1 or i == b:
            print(i)
        elif i < b-1:
            print(i, end=" ")

a = int(input())
b = int(input())
c = int(input())
multiples(a,b,c)

# Same issue here:
# Function naming, parameter naming, and type hinting.

# Have a look how I managed to name the variables in the solution
# and how to handle the selection.