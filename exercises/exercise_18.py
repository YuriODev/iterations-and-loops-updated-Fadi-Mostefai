# Your solution to Exercise 18
def errors(n):
    sum = 0
    for _ in range(n):
        error = int(input())
        sum += error
    return sum

n = int(input())
print(errors(n))

# Same issue here:
# Function naming, parameter naming, and type hinting.