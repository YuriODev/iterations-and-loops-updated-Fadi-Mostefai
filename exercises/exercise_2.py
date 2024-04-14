# Your solution to Exercise 2
def num(n,m):
    if m == 0:
        print("\n")
    for _ in range(m):
        print(n, end=" ")

n = int(input())
m = int(input())

num(n,m)

# Same issue here:
# Function naming, parameter naming, and type hinting.