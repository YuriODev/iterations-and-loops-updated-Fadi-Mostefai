# Your solution to Exercise 28

def product(a,b):
    sum = 0
    for _ in range(a):
        sum += b
    return sum

a = int(input())
b = int(input())
print(product(a,b))

# Same Issue:
# Function naming, parameter naming, and type hinting, sum variable